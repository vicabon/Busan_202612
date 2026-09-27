# Update README.md
readme_content = """# 韓國釜山2026年12月自由行全方位指南：住宿評比 ＆ 百大美食 (README.md)

本專案專為 **2026年12月3日 ～ 12月8日（5天5夜）韓國釜山雙人自由行** 規劃，完整整合：
1. **住 (Hotel - Agent)**：跨 5 大平台（Agoda, Booking, Trip.com, Tripadvisor, Google Maps）大數據住宿評比、價格比對與加權平均口碑。
2. **食 (Food - 100 Great Places)**：釜山觀光公社官方評選 **100 Great Places to Eat in Busan**，詳細標記 **Blue Ribbon Survey (藍絲帶美食調查評級)**、中英韓三語店名、Naver Map 導航地址與飲食種類。
3. **Web Portal (GitHub Pages)**：電腦與手機皆宜瀏覽的現代化響應式雙主軸導覽系統。

---

## 🌐 線上瀏覽與核心成果檔案

| 檔案名稱 | 說明 |
| :--- | :--- |
| **[index.html](index.html)** | **GitHub Pages 線上互動入口**：分頁切換「🏨 住宿評比 (Hotel)」與「🍽️ 釜山100選美食 (Food)」 |
| **[FOOD.md](FOOD.md)** | **Visit Busan 100選美食完整指南**（包含藍絲帶數量、料理種類、中英韓地址與營業時間） |
| **[BUSAN_100_GREAT_PLACES_TO_EAT.md](BUSAN_100_GREAT_PLACES_TO_EAT.md)** | 原始 100 家餐廳資料卡與官方專頁連結 |
| **[韓國釜山2026年12月住宿評比與比價總表.xlsx](韓國釜山2026年12月住宿評比與比價總表.xlsx)** | **主要住宿交付表**：包含 6 個分頁與各網站 Reviews 數加權總平均 |
| **[AGENT.md](AGENT.md)** / **[AGENT.html](AGENT.html)** | 規劃設計思考、系統架構流程與各平台欄位規則解構說明 |
| **[SKILL.md](SKILL.md)** / **[SKILL.html](SKILL.html)** | 專案技術棧手冊（PDF幾何逆向、異質數據對齊、網路爬蟲、雙語實體融合） |

---

## 🏨 住宿篩選條件與成果

- **旅遊日期**：2026/12/3 ～ 2026/12/8 (5 晚, 2 位成人)
- **每晚預算**：0 ～ 5,000 NTD (5 晚總額 25,000 NTD 以內)
- **星級門檻**：3 星級以上 (含 3星、4星、5星豪華飯店)
- **客戶評比**：8.0+ 優秀 (Excellent)
- **位置評比**：8.0+ 優秀 (近地鐵、海灘、商圈)
- **加權總平均**：$$\text{總平均客戶評比} = \frac{\sum (\text{各網站評分} \times \text{該網站 Review 數})}{\sum \text{各網站 Review 數}}$$

---

## 🍽️ 釜山美食指南專區 (Visit Busan 100選 & Blue Ribbon Survey)

本專案自釜山觀光公社官方網站爬取並整理 100 家代表性餐廳：
- 🎀🎀 **2 個藍絲帶 (Top Gourmet)**：極力推薦專程造訪之頂級料理名店。
  - *代表名店*：海雲台著名母牛排骨 (`Haeundae somunnan amso galbijip`)、奶奶蜆湯 (`Halmae jaecheopguk`)、BLACKUP COFFEE、HYTTE ROASTERY、Momos 咖啡。
- 🎀 **1 個藍絲帶 (Recommended)**：深受在地饕客認可之優質人氣美食。
  - *代表名店*：廣安里 Ton shou 炸豬排、西面機張手工刀削麵、合川豬肉湯飯、Ops 麵包坊。
- ⭐ **官方推薦在地老店 (Local Picks)**：承載釜山歷史與常民滋味之必訪經典。

所有餐廳皆附上韓文道路名地址，抵達釜山時可直接複製至 **Naver Map** 或 **Kakao Map** 迅速導航！
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

# Update SKILL.md
skill_content = """# 專案技能清單與技術庫 (SKILL.md)

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
    $$\text{加權平均評分} = \frac{\sum (S_i \times R_i)}{\sum R_i}$$

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
"""

with open('SKILL.md', 'w', encoding='utf-8') as f:
    f.write(skill_content)

print("README.md and SKILL.md updated successfully!")
