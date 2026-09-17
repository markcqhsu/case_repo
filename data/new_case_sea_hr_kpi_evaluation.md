<!--
新案例範本。複製這份檔案（例如 new_case.md），依格式填寫內容，
再執行 `python3 scripts/import_case.py new_case.md` 就會自動加進 data/cases.json。
也可以直接把填好的內容整段貼給 Claude，請它幫你匯入並上架。
每個欄位前面的「## 標籤」不要修改，內容寫在該行後面或下一行皆可。
清單類欄位（例如 執行流程、主要功能）請用 "- " 開頭，一行一項。
不是每個欄位都要填，留空的欄位不會出現在網頁上，案例內容形式本來就不需要完全一樣。
網站是中英雙語（右上角可切換），這份範本請先用中文填寫；
匯入後系統會先把中文內容複製一份當作英文版佔位，記得之後請 Claude 或自己翻成英文。
-->

## 案例標題
跨國員工績效自評與多階主管評核 Web App

## 案例摘要
運用 Google Sheets、Google Apps Script 與網頁前端技術，建立一套適用於東南亞多國據點的員工績效考核系統。系統支援員工個人化 KPI、自評、Leadership／Individual 差異化評分、多階 Reviewer 依序評核、主管平均給分及多語言介面；員工不需具備公司 Google 帳號，即可透過工號與 PIN 登入完成考核。

## 案例分類
人力資源管理、績效管理、流程數位化、跨國管理、內部系統開發

## 需求單位
東南亞總部人力資源單位

## 負責單位
東南亞總部人力資源單位

## 案例負責人
禤珮宜

## 案例狀態
已完成可操作測試版本，持續進行多語言配對、權限規則與正式上線驗證

## 適用地區
東南亞六國據點：柬埔寨、緬甸、越南、泰國、印尼、馬來西亞，以及總部管理端

## 網站連結


## 影片介紹


## 畫面截圖
assets/sea-hr-kpi-self-evaluation-demo.jpg

## 問題背景
公司各國廠區人數差異大，單一據點約 13 至 400 人，且並非所有員工都有公司 Google 帳號。考核 KPI 採逐人設定，每位員工的 KPI 項目、權重與 Reviewer 路徑皆可能不同；Reviewer 1 至 Reviewer 3 必須依序評核，且 Reviewer 與 Reviewee 不一定隸屬相同廠區。原先以 Google Form 規劃時，難以同時處理個人化 KPI、自動帶入員工資料、差異化評分、多階簽核及跨國語言需求，而付費 AppSheet 亦不符合專案的成本條件。

## 核心問題
如何在不增加軟體授權成本、員工沒有公司 Google 帳號的條件下，建立一套能支援個人化 KPI、跨廠區多階主管依序評核、不同職務定位評分公式、多語言操作、資料追蹤及重複送出控管的績效考核工具。

## 解決方案
以 Google Sheets 作為資料庫，搭配 Google Apps Script Web App 建立員工自評與 Reviewer 評核兩套網頁介面。資料結構拆分為員工主檔、KPI 指派、登入權限、自評主檔、自評明細、Reviewer 主檔、評核指派、主管評核主檔及 KPI 評核明細等工作表；員工與 Reviewer 以 ID、PIN 及啟用狀態登入。系統依 Employee Type 自動套用評分架構，並以 Submission ID、Reviewer Level、狀態欄位與伺服器端驗證維持流程順序和資料完整性。

## 執行流程
- 釐清制度規則：確認 KPI 採逐人設定、評分範圍為 0 至 100 的整數，以及 Leadership／Individual 的評分組成。
- 建立 Google Sheets 資料架構：完成 01_Employee_Master 至 09_KPI_Review_Response 等主檔、指派表與結果表。
- 建立員工登入與自評頁面：透過 Emp ID 與 Access PIN 登入，自動顯示基本資料與個人 KPI。
- 建立兩頁式自評流程：第一頁填寫 KPI，第二頁填寫 Teamwork 及依 Employee Type 決定是否顯示 Leadership。
- 建立送出前檢核：驗證必填欄位、整數分數、KPI 權重及加權後的自評總分。
- 建立 Reviewer 管理與評核流程：設定 Reviewer 1 至 3，依序開放待評案件，並顯示員工自評與前階 Reviewer 紀錄。
- 建立最終評分邏輯：各階 Reviewer 獨立留存分數與評語，完成後以所有 Reviewer 分數平均作為主管評核平均給分。
- 建立多語言介面：支援 English、Thai、Vietnamese、Malay、Nepali、Indonesian、Burmese、Khmer，並依各國需求搭配中文或英文。
- 進行錯誤排除與測試：處理 Spreadsheet ID、欄位名稱、百分比格式、送出按鈕、重複送出、員工類型及工作表同步等問題。
- 建立手動同步功能：由 01_Employee_Master 將新增的 Active 員工安全地補入 03_Access_Control 與 07_Review_Assignment，不重排或覆蓋既有資料。
- 儲存程式、執行 testConfiguration、更新 Web App deployment，並以不同員工類型與 Reviewer 層級進行端到端測試。

## 主要功能
- 無 Google 帳號登入｜員工及 Reviewer 可使用 ID 與 PIN 登入，不必具備公司 Google 帳號。
- 個人化 KPI｜依 Emp ID 載入每位員工專屬的 KPI Item、Weight、Score 與 Comment。
- 員工資料確認｜自動顯示廠區、工號、姓名、部門、單位、職稱及員工定位，讓員工確認或填寫更正說明。
- 兩頁式自評｜第一頁為 KPI，第二頁為 Teamwork、Leadership 及其他建議，降低單頁資訊量。
- 差異化評分｜Individual 為 KPI 80%＋Teamwork 20%；Leadership 為 KPI 60%＋Teamwork 20%＋Leadership 20%。
- 分數驗證｜所有評分限填 0 至 100 的整數，並檢查 KPI 權重合計是否為 100%。
- 送出前確認｜在正式送出前顯示各構面分數、占比及自評總分，供員工再次核對。
- 重複送出控管｜Self-Evaluation Status 為 Submitted 時阻止再次進入自評，後端送出時亦再次檢查狀態。
- 多階 Reviewer 流程｜Reviewer 1 至 3 依序評核，後階 Reviewer 可查看員工自評及前階 Reviewer 的分數與評語。
- Reviewer 待辦清單｜在 Reviewer 頁首顯示待評核總筆數，並僅開放目前應由該 Reviewer 處理的案件。
- 主管評分彙整｜保留各階 Reviewer 獨立紀錄，全部完成後計算主管評核平均給分。
- 多語言介面｜支援八種主要語言，並依語言群組顯示「當地語言＋中文」或「當地語言＋英文」。
- 安全同步｜以手動函式補入新進員工，避免使用動態公式造成 Emp ID 與 PIN／Reviewer 指派錯位。

## AI 的應用方式
- 將跨國績效制度需求轉換為可執行的資料表結構、欄位規格與系統流程。
- 協助產出及迭代 Google Apps Script、HTML、CSS 與 JavaScript 程式碼。
- 依錯誤畫面與 Execution log 判讀 Spreadsheet ID、欄位缺漏、百分比格式及前後端事件問題。
- 將 Leadership／Individual、KPI 權重、多階 Reviewer 等制度規則轉換為驗證與計分邏輯。
- 設計多語言介面、雙語搭配方式、欄位文字、提示語、錯誤訊息及送出提醒。
- 協助進行程式語法檢查、重複函式檢查、流程測試與部署步驟整理。
- 在開發過程中即時提供操作教學，使非資訊背景的人資人員可自行維護與測試系統。

## 使用工具
- Google Sheets｜作為員工、KPI、登入權限、Reviewer 指派及評核結果的資料庫。
- Google Apps Script｜執行登入驗證、資料讀寫、計分、狀態控管、流程管理與 Web App 部署。
- HTML／CSS／JavaScript｜建立員工自評與 Reviewer 評核網頁、互動式檢核及多語言介面。
- Google Apps Script Execution log｜追蹤伺服器端錯誤並驗證程式執行結果。
- 生成式 AI｜協助需求分析、系統設計、程式產出、除錯、翻譯及文件化。

## 執行成果
- 完成可登入、可讀取個人 KPI、可計分並可送出的員工自評 Web App 測試版本。
- 完成 Leadership 與 Individual 兩種評分架構及條件式 Leadership 區段。
- 完成 Reviewer 1 至 3 依序評核、前階結果查閱、獨立紀錄及平均給分流程。
- 完成 9 張核心 Google Sheets 工作表的資料架構與欄位驗證機制。
- 完成送出前分數檢核、必填驗證、0 至 100 整數限制及重複送出阻擋。
- 完成 Reviewer 待評核總筆數顯示及員工／Reviewer 專用登入權限管理。
- 完成八種語言的介面架構，並建立不同語言搭配中文或英文的呈現規則。
- 完成新增員工手動同步至 Access Control 與 Review Assignment 的安全機制。
- 在不採購 AppSheet 或其他付費 HR 系統的情況下，驗證 Google Workspace 工具可支援此績效流程。

## 產生價值
- 對人資單位｜將分散的員工、KPI、Reviewer 與評核結果集中管理，降低人工製表、追蹤及彙整負擔。
- 對員工｜不需公司 Google 帳號即可操作，並可在送出前清楚確認個人資料、KPI、各構面分數及總分。
- 對主管｜提供明確的待辦清單、前階評核資訊及一致的評分介面，支援跨廠區依序評核。
- 對公司｜以低成本方式建立可追溯、可複製、可跨國使用的績效考核流程，提升制度一致性及資料透明度。


## 可複製與延伸應用
- 複製整份 Google Sheet 與綁定的 Apps Script，即可建立下一個半年考核週期的獨立版本。
- 可調整 Employee Master、KPI Assignment 及 Review Assignment，快速套用至不同國家、廠區或人數規模。
- 可擴充正式的退回修改、HR 重新開放、Email 通知、逾期提醒及進度儀表板功能。
- 可增加考勤、核心職能、價值觀、人才盤點或校準會議等績效構面。
- 相同的 ID／PIN、個人化題目及多階審核架構，可延伸至訓練需求調查、試用期考核、晉升評核及內部申請流程。
- 多語言字典可獨立維護，未來可增加其他國家語言或調整第二顯示語言。

## 使用限制與注意事項
- Google Apps Script 仍受每日配額、單次執行時間與大量同時存取影響，正式上線前應依最高人數進行情境測試。
- PIN 為輕量型登入機制，不等同企業級 SSO；Google Sheet、Apps Script 與部署權限必須限制於必要管理者。
- Emp ID、Reviewer ID、欄位名稱及工作表名稱必須保持唯一且一致，否則可能造成登入、指派或資料寫入錯誤。
- 每位員工的 Active KPI 權重合計必須為 100%，Weight 儲存格式需統一，避免 35 與 35% 被重複換算。
- 新增員工目前採手動執行 syncEmployeeRecords，不使用自動 trigger；同步後仍需由 HR 設定 PIN、啟用狀態及 Reviewer。
- Submitted 後若需修改，不應只把狀態改回 Not Submitted，否則可能產生新的 Submission ID 及重複明細；應建立正式的 Reopen 流程。
- 修改 Code.gs、Index.html、Reviewer.html 或 Translations.html 後，必須建立 New version 並重新 Deploy，正式網址才會載入新版。
- 多語言文字應由各國 HR 或母語使用者複核，以確保制度用語與當地語意正確。
- 複製 Google Sheet 後，仍須檢查 Spreadsheet ID、deployment、授權、網址及資料清除範圍，避免沿用前一期敏感資料。

## 成功關鍵
先將績效制度規則、員工定位、計分公式、Reviewer 順序與資料責任定義清楚，再進行程式設計；同時維持工作表欄位標準化、以伺服器端進行關鍵驗證，並使用不同國家、員工類型及 Reviewer 層級進行完整端到端測試。人資需保有主檔、權限、Reviewer 指派與版本部署的治理責任，才能讓低成本工具長期穩定運作。

## 案例關鍵字
績效考核、員工自評、KPI、Google Apps Script、Google Sheets、Web App、多階主管評核、跨國人資、多語言、流程數位化、Reviewer、Leadership、Individual
