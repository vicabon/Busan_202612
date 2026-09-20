# 專案技能清單與技術庫 (SKILL.md)

本文件詳列在「**2026年12月韓國釜山住宿大數據分析專案**」中所運用之各項自動化、數據科學、逆向解析及工程技能。

---

## 1. 核心技能清單 (Core Skill Registry)

### Skill 1: 進階 PDF 逆向版面結構分析 (Advanced PDF Layout & Geometry Parsing)
- **技術庫**：`pdfplumber`, `pypdf`
- **核心能力**：
  - **幾何向量路徑聚類**：從 PDF 原始路徑物件 (`curves`, `rects`) 中過濾特定寬高比例之幾何形狀（如 Booking.com 飯店星星圖標），透過 Y 軸坐標相鄰判定星級數量。
  - **2D 文字區塊配對**：解決網頁列印版 PDF 左右欄分離、文字串流非線性問題，依據垂直 bounding box 精確重組卡片資訊。

### Skill 2: 多平台異質資料正規化 (Cross-Platform Data Normalization)
- **技術庫**：Python `re`, `unicodedata`
- **核心能力**：
  - **價格維度轉換**：自動識別「每晚房價 (per night)」與「5晚總額 (in total)」，並分離稅金外加與含稅標記。
  - **評分尺規對齊**：支援 10 分制（Agoda、Booking、Trip.com）與 5 分制（Tripadvisor、Google Map）之語意映射與數據對齊。
  - **特殊字符編碼解碼**：正確解析 Trip.com 使用之專屬 Unicode 自訂符號（Private Use Area）。

### Skill 3: 實體識別與跨來源模糊對齊 (Entity Resolution & Fuzzy Matching)
- **技術庫**：自研字串前處理、正規劃 Token 集合與 Jaccard 相似度演算法
- **核心能力**：
  - 去除地名前綴、連字號、分詞變體（如 `Wyndham Grand Busan Ijin` 與 `Wyndham Grand Busan`）。
  - 將多達 200 多個跨平台房源實體歸納至統一的總結比價清單。

### Skill 4: 商業級 Excel 報表自動化構建 (Automated Spreadsheet Engineering)
- **技術庫**：`openpyxl`
- **核心能力**：
  - 支援多工作表 (Tab/Sheet) 依功能劃分，設定各品牌代表色系（Booking 深藍、Agoda 經典紅、Trip 天空藍、Tripadvisor 森林綠、Google 活力橘）。
  - 斑馬紋交錯背景、動態自適應欄寬計算、專業微軟正黑體字型階層與外框格線優化。

### Skill 5: 網路情報即時檢索與驗證 (Web Intelligence & Grounding)
- **技術庫**：Web Search Engine, 地理資訊檢索
- **核心能力**：
  - 快速調取 Tripadvisor 與 Google Maps 針對釜山指標飯店之最新評比、評論總量與交通關鍵字。
