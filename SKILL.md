# 專案技能清單與技術庫 (SKILL.md)

本文件詳列在「**2026年12月韓國釜山住宿大數據分析與百大美食指南專案**」中所運用之各項自動化、數據科學、逆向解析及工程技能。

---

## 1. 核心技能清單 (Core Skill Registry)

### Skill 1: 進階 PDF 逆向版面結構分析 (Advanced PDF Layout & Geometry Parsing)
- **技術庫**：`pdfplumber`, `pypdf`
- **核心能力**：
  - **幾何向量路徑聚類**：從 PDF 原始路徑物件 (`curves`, `rects`) 中過濾特定寬高比例之幾何形狀（如 Booking.com 飯店星星圖標），透過 Y 軸坐標相鄰判定星級數量。
  - **2D 文字區塊配對**：解決網頁列印版 PDF 左右欄分離、文字串流非線性問題，依據垂直 bounding box 精確重組卡片資訊。

### Skill 2: 動態多語系觀光網絡爬蟲與資料抽取 (Multilingual Web Scraping & Ingestion)
- **技術庫**：`requests`, `BeautifulSoup4`
- **核心能力**：
  - **雙語版面自動鏡像爬取**：自動並行請求 Visit Busan 官方網站之英文與韓文端點，以非同步/分頁管線抓取 100 家餐廳完整圖文資訊。
  - **圖形徽章語意抽取 (Icon Badge Semantic Extraction)**：精準識別 HTML 中隱藏之 `img[title]` 與 Ribbon 列表結構，解析出各店鋪獲得之 **Blue Ribbon Survey (藍絲帶)** 評級數量。

### Skill 3: 多平台異質資料正規化 (Cross-Platform Data Normalization)
- **技術庫**：Python `re`, `unicodedata`
- **核心能力**：
  - **價格維度轉換**：自動識別「每晚房價 (per night)」與「5晚總額 (in total)」，並分離稅金外加與含稅標記。
  - **評分尺規對齊**：支援 10 分制（Agoda、Booking、Trip.com）與 5 分制（Tripadvisor、Google Map）之語意映射與數據對齊。
  - **加權平均演算法**：設計以有效 Review 總數為權重之精確數學計算公式：
    $$	ext{加權平均評分} = rac{\sum (S_i 	imes R_i)}{\sum R_i}$$

### Skill 4: 實體識別與跨來源雙語對齊 (Entity Resolution & Bilingual Alignment)
- **技術庫**：自研字串前處理、正規劃 Token 集合與 Jaccard 相似度演算法
- **核心能力**：
  - 跨平台飯店名稱匹配（解決別名、分詞變體問題）。
  - 美食名單英韓雙語實體一對一綁定，建立包含英韓店名、英文地址與 Naver Map 專用韓文道路名地址之高可用資料結構。

### Skill 5: 商業級 Excel 報表自動化構建 (Automated Spreadsheet Engineering)
- **技術庫**：`openpyxl`
- **核心能力**：
  - 支援多工作表 (Tab/Sheet) 依功能劃分，設定各品牌代表色系（Booking 深藍、Agoda 經典紅、Trip 天空藍、Tripadvisor 森林綠、Google 活力橘）。
  - 斑馬紋交錯背景、動態自適應欄寬計算、專業微軟正黑體字型階層與外框格線優化。

### Skill 6: 現代化響應式雙主軸入口網站開發 (Responsive Web Portal Development)
- **技術庫**：HTML5, CSS3 Grid/Flexbox, Vanilla JavaScript
- **核心能力**：
  - 打造「住 (Hotel)」與「食 (Food)」雙主軸頂部無縫切換系統。
  - **雙模態適配**：電腦端展示高密度排版表格，手機端自動切換為高質感觸控卡片串流。
  - **前端即時搜尋與多條件篩選**：支援雙語關鍵字、料理類型、藍絲帶數量分級動態過濾。
