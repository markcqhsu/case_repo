#!/usr/bin/env python3
"""將 data/case_template.md 格式的案例文件匯入 data/cases.json。

用法：
  python3 scripts/import_case.py 案例檔案.md
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_JSON = ROOT / "data" / "cases.json"

SECTION_MAP = {
    "案例標題": "title",
    "案例摘要": "summary",
    "案例分類": "category",
    "需求單位": "unit_request",
    "負責單位": "unit_owner",
    "案例負責人": "author",
    "案例狀態": "status",
    "適用地區": "region",
    "網站連結": "url",
    "畫面截圖": "screenshot",
    "問題背景": "problem_background",
    "核心問題": "core_problem",
    "解決方案": "solution",
    "執行流程": "process",
    "主要功能": "features",
    "AI 的應用方式": "ai_usage",
    "使用工具": "tools",
    "執行成果": "results",
    "產生價值": "value",
    "可複製與延伸應用": "extensions",
    "使用限制與注意事項": "limitations",
    "成功關鍵": "success_key",
    "案例關鍵字": "keywords",
}

LIST_FIELDS = {"process", "ai_usage", "results", "extensions", "limitations"}
PAIR_LIST_FIELDS = {"features", "tools", "value"}
DELIM_LIST_FIELDS = {"category", "keywords"}


def parse_sections(text):
    lines = text.splitlines()
    sections = {}
    current = None
    buf = []
    for line in lines:
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current is not None:
                sections[current] = buf
            current = m.group(1)
            buf = []
        elif line.strip().startswith("<!--") or line.strip().startswith("-->"):
            continue
        else:
            buf.append(line)
    if current is not None:
        sections[current] = buf
    return sections


def clean_block(lines):
    text = "\n".join(lines).strip()
    return text


def parse_list(lines):
    items = []
    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
    return items


def parse_pair_list(lines):
    items = []
    for entry in parse_list(lines):
        if "｜" in entry:
            name, desc = entry.split("｜", 1)
            items.append({"name": name.strip(), "desc": desc.strip()})
        elif "|" in entry:
            name, desc = entry.split("|", 1)
            items.append({"name": name.strip(), "desc": desc.strip()})
        else:
            items.append(entry.strip())
    return items


def parse_delim_list(lines):
    text = clean_block(lines)
    if not text:
        return []
    return [t.strip() for t in re.split(r"[、,]", text) if t.strip()]


def build_case(sections, existing_count):
    data = {}
    for label, key in SECTION_MAP.items():
        raw = sections.get(label, [])
        if key in LIST_FIELDS:
            data[key] = parse_list(raw)
        elif key in PAIR_LIST_FIELDS:
            data[key] = parse_pair_list(raw)
        elif key in DELIM_LIST_FIELDS:
            data[key] = parse_delim_list(raw)
        else:
            data[key] = clean_block(raw)

    data["id"] = f"case-{existing_count + 1:03d}"
    return data


def main():
    if len(sys.argv) != 2:
        print("用法：python3 scripts/import_case.py 案例檔案.md")
        sys.exit(1)

    src = Path(sys.argv[1])
    if not src.exists():
        print(f"找不到檔案：{src}")
        sys.exit(1)

    cases = json.loads(CASES_JSON.read_text(encoding="utf-8")) if CASES_JSON.exists() else []

    sections = parse_sections(src.read_text(encoding="utf-8"))
    case = build_case(sections, len(cases))

    if not case.get("title"):
        print("警告：案例標題是空的，請檢查檔案格式。")
        sys.exit(1)

    cases.append(case)
    CASES_JSON.write_text(
        json.dumps(cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"已加入案例：{case['title']}（id: {case['id']}）")
    print(f"寫入：{CASES_JSON}")


if __name__ == "__main__":
    main()
