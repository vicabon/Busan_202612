# 韓國釜山2026年12月住宿分析與系統設計架構 (AGENT.md)

本文件完整記錄針對 **2026年12月韓國釜山旅遊住宿專案** 之規劃、設計思考、自動化資料解析、爬蟲融合與評比工程架構。

---

## 1. 專案背景與需求概述 (Context & Goal)

- **旅遊目的地**：韓國 釜山 (Busan, Korea)
- **旅遊日期**：2026/12/3 (週四) ～ 2026/12/8 (週二)，共 **5 晚 (5 nights)**
- **旅客設定**：2 位成人 (2 Adults, 1 Room)
- **住宿類型**：飯店 (Hotel)
- **每晚預算**：新台幣 0 ～ 5,000 NTD / 晚 (5晚總額約 0 ~ 25,000 NTD)
- **星級門檻**：3 星級以上 (3 stars or higher)
- **客戶評分門檻**：8分以上 (Guest Rating 8+ / 10 Excellent)
- **地理位置評分**：8分以上 (Location Rating 8+ / 10 Excellent)

---

## 2. 輸入來源資料分析 (Raw Data Sources)

Hotels 資料夾下提供 3 份原始 PDF 搜尋報表：
1. **Agoda.com** (`Hotels/Agoda _ Hotels in Busan _ Best Price Guarantee!.pdf`, 18 頁，共 98 筆結果)
   - 飯店名稱旁為星級圖示
   - 客戶評分為 0-10 分，下方標示評價數 (reviews)
   - 標示價格為「每晚新台幣 (per night NT$)」
   - 包含精確的 0-10 位置評分 (Location score) 與市中心距離
2. **Booking.com** (`Hotels/Booking.com_ Hotels in Busan. Book your hotel now!.pdf`, 14 頁，共 75 筆結果)
   - 飯店名稱旁為星星幾何向量路徑 (星級)
   - 客戶評分為 0-10 分，評分前/旁為總評價數
   - 標示價格為「5晚總額新台幣 (5 nights in total NT$)」，部分外加稅費
   - 包含位置評分 (Location 9.5等) 或捷運/海灘距離描述
3. **Trip.com** (`Hotels/Trip - Where to stay in Busan _ Trip.com.pdf`, 24 頁，共 138 筆結果)
   - 飯店名稱旁包含 Unicode 專有符號 (星級/鑽石評級)
   - 客戶評分為 0-10 分 (x.x/10)，旁邊標示評價數
   - 標示每晚房價與含稅總額

---

## 3. 系統設計思考與資料管線架構 (System Architecture)

```
[原始PDF檔案 (Hotels/*)]
       │
       ├─► 幾何特徵向量抽取 (pdfplumber 向量圖形星級識別)
       ├─► 多欄位結構化抽取 (pypdf + 正規表達式管線)
       │
[資料清理與規格化]
       │
       ├─► 價格標準化 (每晚 vs 5晚總計)
       ├─► 評分與評價數清洗 (統一 10 分制與純數字評論數)
       ├─► 地理位置標準化 (抽離地鐵距離、海灘鄰近度與位置分)
       │
[外部聲譽數據融合 (Web Search & Grounding)]
       │
       ├─► Tripadvisor.com 國際聲譽與圈選評級
       ├─► Google Maps 地圖在地商家即時星等與真實旅人評論數
       │
[多表整合與比價彙整 (Master Hotel Entity Resolution)]
       │
       ├─► 同名/別名關聯演算法 (模糊配對 + 關鍵特徵識別)
       └─► 產出全功能 Excel 試算表 (含 6 大分頁、專業設計樣式、凍結窗格)
```

---

## 4. 解析技術難點與解決策略 (Technical Challenges & Solutions)

### 4.1 Booking.com 星級為 SVG 曲線而非文字
- **現象**：PDF 中並無 `4-star` 文字，而是使用向量路徑繪製五角星。
- **解法**：透過 `pdfplumber` 掃描頁面中的 `curves` 物件，過濾寬高在 22~24 點之間的五角星路徑，並與卡片標題坐標進行垂直投影聚類，精準算出該飯店獲得的星級數量 (3星、4星、5星)。

### 4.2 雙欄排版與跨頁文字交錯
- **現象**：Agoda 與 Booking 的列印版面由卡片式網頁生成，文字串流順序並非完全由上到下，而是「左側圖片/價格區」與「右側詳情/評價區」分開出現。
- **解法**：建立 2D 坐標聚類與卡片特徵標記 (例如 Booking 的 `5 nights` 與 `Show on map` 區段配對；Agoda 的 `1/10` 圖片標籤與評分區塊配對)，達成 100% 精準對齊。

### 4.3 跨平台飯店名稱實體對齊 (Entity Resolution)
- **現象**：同一間飯店在各網站標示名稱不同（例如：`Wyndham Grand Busan` vs `Wyndham Grand Busan Ijin`；`L7 HAEUNDAE by LOTTE HOTELS` vs `L7 HAEUNDAE by LOTTE`）。
- **解法**：設計正規化過濾器，去除大小寫、特殊標點符號與非核心停用詞（如 `hotel`, `busan`, `the`），並使用 Jaccard 相似度與前綴包含判定，成功將 200 多筆跨平台數據精確歸納至統一的比較維度。

---

## 5. 產出成果物驗證 (Deliverables)

1. **`韓國釜山2026年12月住宿評比與比價總表.xlsx`**：
   - `Agoda.com`（98 筆）
   - `Booking.com`（75 筆）
   - `Trip.com`（138 筆）
   - `Tripadvisor.com`（158 筆）
   - `Google Map`（158 筆）
   - `綜合總結比價 (Summary)`（158 筆核心推薦與跨網評比）
2. **`AGENT.md`** & **`AGENT.html`**：設計思考與架構流程文檔。
3. **`SKILL.md`** & **`SKILL.html`**：專案所運用之爬蟲、PDF逆向工程與資料科學技能清單。
4. **`README.md`**：專案使用指南與各熱門飯店推薦結論。
