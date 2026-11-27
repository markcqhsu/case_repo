#!/usr/bin/env python3
"""由繁體中文內容自動產生簡體中文版（zh-CN）。

每次新增或修改案例（data/cases.json）或更新紀錄（data/changelog.json）後都要重跑一次：
    python3 tools/build_zhcn.py

需要的套件（裝在專案外的 venv 即可）：
    pip install opencc-python-reimplemented

規則：
- 案例：把每筆案例的 i18n.zh 轉成 i18n["zh-CN"]（台灣用語 → 大陸用語，tw2sp）。
- 單位名稱（需求單位、負責單位）只做逐字繁簡轉換，不換詞，避免組織名稱被改成別的詞。
- 案例負責人姓名保持原樣，不轉換。
- 更新紀錄：每筆 notes 另存一份 notes_cn。
"""
import json
import re
import sys
from pathlib import Path

try:
    import opencc
except ImportError:
    sys.exit('找不到 opencc，請先安裝：pip install opencc-python-reimplemented')

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / 'data' / 'cases.json'
CHANGELOG = ROOT / 'data' / 'changelog.json'

phrase = opencc.OpenCC('tw2sp')   # 台灣正體 → 簡體（含詞彙）
chars = opencc.OpenCC('t2s')      # 只轉字，不換詞

# 不做逐字以外轉換的欄位 / 完全不轉換的欄位
CHAR_ONLY_FIELDS = {'unit_request', 'unit_owner'}
KEEP_FIELDS = {'author'}

cases = json.loads(CASES.read_text(encoding='utf-8'))

# 內文中若出現單位名稱，也用逐字轉換保護起來
protected = sorted(
    {c['i18n']['zh'].get(k, '') for c in cases for k in CHAR_ONLY_FIELDS} - {''},
    key=len, reverse=True)

# opencc 詞彙轉換會誤轉或不夠道地的詞，這裡直接指定結果
CUSTOM = {
    '開機率': '开机率', '程序': '程序', '堆疊': '堆叠', '紀錄': '记录',
    '排程': '排程', '查詢': '查询', '文字': '文字', '執行': '执行',
    '品質': '质量', '棧板': '托盘', '貨櫃': '集装箱', '資料整合': '数据整合',
    '支援': '支援',
}

# 站內固定分類標籤
CATEGORY_MAP = {
    '流程自動化': '流程自动化', '內部管理工具': '内部管理工具',
    '資料整合與分析': '数据整合与分析', '業務支援': '业务支援',
    '生產管理': '生产管理', '職安環保': '职安环保', '品保工作流程': '品保工作流程',
    '教育訓練與文宣': '教育培训与宣传', '工程管理': '工程管理', '小工具': '小工具',
}

_hold_words = sorted(set(protected) | set(CUSTOM), key=len, reverse=True)


def convert_text(s):
    slots = []

    def hold(m):
        w = m.group(0)
        slots.append(CUSTOM[w] if w in CUSTOM else chars.convert(w))
        return f'\ue000{len(slots) - 1}\ue001'

    s = re.sub('|'.join(map(re.escape, _hold_words)), hold, s)
    s = phrase.convert(s)
    return re.sub('\ue000(\\d+)\ue001', lambda m: slots[int(m.group(1))], s)


def convert(value, field=None):
    if field in KEEP_FIELDS:
        return value
    if field == 'category':
        return [CATEGORY_MAP.get(v, convert_text(v)) for v in value]
    if isinstance(value, str):
        return chars.convert(value) if field in CHAR_ONLY_FIELDS else convert_text(value)
    if isinstance(value, list):
        return [convert(v, field) for v in value]
    if isinstance(value, dict):
        return {k: convert(v, k) for k, v in value.items()}
    return value


for c in cases:
    c['i18n']['zh-CN'] = {k: convert(v, k) for k, v in c['i18n']['zh'].items()}

CASES.write_text(json.dumps(cases, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

log = json.loads(CHANGELOG.read_text(encoding='utf-8'))
for e in log['entries']:
    e['notes_cn'] = convert_text(e['notes'])
CHANGELOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

print(f'zh-CN 已產生：{len(cases)} 個案例、{len(log["entries"])} 筆更新紀錄')
