#!/usr/bin/env python3
"""為 data/cases.json 用到的每張截圖產生 600px 寬的 WebP 縮圖，放在 assets/thumbs/。

列表卡片與詳情頁的小縮圖會優先載入這些縮圖，找不到時自動退回原圖。
新增案例後執行一次即可（已存在且比原圖新的縮圖會略過）：
  python3 scripts/make_thumbs.py

需要 cwebp（macOS: brew install webp）。
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_JSON = ROOT / "data" / "cases.json"
THUMB_DIR = ROOT / "assets" / "thumbs"
WIDTH = 600


def image_width(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", str(path)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if "pixelWidth" in line:
            return int(line.split()[-1])
    return None


def main():
    if not shutil.which("cwebp"):
        sys.exit("找不到 cwebp，請先安裝（brew install webp）")
    cases = json.loads(CASES_JSON.read_text(encoding="utf-8"))
    sources = set()
    for c in cases:
        if c.get("screenshot"):
            sources.add(c["screenshot"])
        for s in c.get("screenshots") or []:
            if s:
                sources.add(s)

    THUMB_DIR.mkdir(parents=True, exist_ok=True)
    made = 0
    for rel in sorted(sources):
        src = ROOT / rel
        if not src.exists():
            print(f"略過（找不到檔案）：{rel}")
            continue
        dst = THUMB_DIR / (src.stem + ".webp")
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            continue
        w = image_width(src) if shutil.which("sips") else None
        resize = ["-resize", str(WIDTH), "0"] if (w is None or w > WIDTH) else []
        subprocess.run(["cwebp", "-quiet", "-q", "80", *resize, str(src), "-o", str(dst)], check=True)
        made += 1
    print(f"完成：新產生 {made} 張縮圖，共 {len(sources)} 張來源圖片")


if __name__ == "__main__":
    main()
