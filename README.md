# AI / 自動化案例庫

分享用 AI 或自動化工具解決廠內流程問題的實際案例，可搜尋、依工具標籤篩選。

## 新增案例

編輯 `data/cases.json`，新增一筆物件：

```json
{
  "id": "唯一代號",
  "title": "案例標題",
  "screenshot": "assets/檔名.png",
  "url": "https://...",
  "author": "製作人姓名",
  "tools": ["使用工具1", "使用工具2"],
  "problem": "解決的問題",
  "design": "設計架構思路",
  "tags": ["分類標籤"]
}
```

畫面截圖放在 `assets/` 資料夾，`screenshot` 欄位填相對路徑。

## 本機預覽

```
python3 -m http.server 8000
```

開啟 http://localhost:8000
