# AI / 自動化案例庫

分享用 AI 或自動化工具解決廠內流程問題的實際案例，可搜尋、依案例分類篩選，支援手機瀏覽。

## 新增案例

兩種方式，擇一即可：

1. **請 Claude 幫忙**：把案例內容（文字＋截圖）直接貼給 Claude，請它轉成資料並上架、推送。
2. **自己維護**：複製 `data/case_template.md`，依格式填寫內容，截圖放進 `assets/`，
   執行：
   ```
   python3 scripts/import_case.py 你的案例檔案.md
   ```
   會自動把新案例加進 `data/cases.json`。

每個案例的欄位不需要完全一樣（例如有些案例沒有「執行流程」或「成功關鍵」），
留空或不寫的欄位不會顯示在網頁上。

## 資料結構

`data/cases.json` 是一個陣列，每筆案例大致包含：

- 基本資料：`title`、`summary`、`screenshot`、`url`、`category`、`unit_request`、`unit_owner`、`author`、`status`、`region`
- 內容：`problem_background`、`core_problem`、`solution`
- 清單類：`process`、`features`、`ai_usage`、`results`、`value`、`extensions`、`limitations`、`keywords`
- `success_key`

清單類欄位可以是純文字陣列（例：`["步驟一", "步驟二"]`），
也可以是「名稱＋說明」的物件陣列（例：`[{"name": "功能一", "desc": "說明"}]`），
兩種格式都能正常顯示，方便不同案例的內容形式。

## 版本與改版紀錄

首頁右上角的版號徽章來自 `data/changelog.json`，點擊可以看到改版紀錄。
正式上線前版號固定為 `v1.0.0`，每次更新只增加改版紀錄項目。

## 本機預覽

```
python3 -m http.server 8000
```

開啟 http://localhost:8000
