import json

with open('visitbusan_100_places.json', 'r', encoding='utf-8') as f:
    en_places = json.load(f)

with open('visitbusan_100_places_kr.json', 'r', encoding='utf-8') as f:
    kr_places = json.load(f)

# Count ribbons
two_ribbons = sum(1 for p in en_places if p['ribbon_count'] == 2)
one_ribbon = sum(1 for p in en_places if p['ribbon_count'] == 1)
zero_ribbon = sum(1 for p in en_places if p['ribbon_count'] == 0)

md = []
md.append("# 韓國釜山2026年12月美食指南：Visit Busan 100選 (FOOD.md)")
md.append("")
md.append("> 本文件為 **2026年12月韓國釜山旅遊專案** 之官方精選美食指南，完整收錄 Visit Busan (釜山觀光公社) 評選之 **100 Great Places to Eat in Busan**。")
md.append("> 結合韓國權威美食評鑑 **Blue Ribbon Survey (藍絲帶調查)** 認證標記、中英韓三語對照、Naver Map 導航道路名地址、特色飲食分類與營業時間。")
md.append("")
md.append("---")
md.append("")
md.append("## 📌 藍絲帶調查 (Blue Ribbon Survey) 評級體系說明")
md.append("")
md.append("Blue Ribbon Survey (블루리본 서베이) 創立於2005年，為韓國歷史最悠久、公信力最高的頂級美食評鑑指南，被譽為「韓國的米其林指南」：")
md.append("- 🎀🎀 **2 個藍絲帶**：在該料理領域具備頂級實力，極力推薦專程造訪（本次收錄共 **" + str(two_ribbons) + "** 家）。")
md.append("- 🎀 **1 個藍絲帶**：口味卓越、深受在地饕客與旅客喜愛之優質名店（本次收錄共 **" + str(one_ribbon) + "** 家）。")
md.append("- ⭐ **釜山官方百大精選 (0 個藍絲帶)**：雖未列入年度藍絲帶評等，但獲釜山觀光公社大力推薦之必吃在地傳統老店或人氣新星（共 **" + str(zero_ribbon) + "** 家）。")
md.append("")
md.append("---")
md.append("")
md.append("## 🗺️ 區域與美食種類精選導覽 (Busan Food Categories)")
md.append("")
md.append("1. **海雲台 (Haeundae) / 廣安里 (Gwangalli)**：")
md.append("   - **海鮮與烤肉**：海雲台著名母牛排骨 (`Haeundae somunnan amso galbijip` 🎀🎀)、Ton shou 頂級日式炸豬排 (`Ton shou` 🎀)。")
md.append("   - **海景咖啡與烘焙**：Ops 經典法式烘焙 (`Ops` 🎀)、MONSIEUR VINCENT 歐式麵包 (`MONSIEUR VINCENT` 🎀)。")
md.append("2. **西面 (Seomyeon) / 田浦咖啡街 (Jeonpo)**：")
md.append("   - **精品咖啡**：BLACKUP COFFEE (`BLACKUP COFFEE` 🎀🎀)、HYTTE ROASTERY (`HYTTE ROASTERY` 🎀🎀)、Werk Roasters (`Werk Roasters` 🎀🎀)。")
md.append("   - **傳統麵食與湯飯**：機張手工刀削麵 (`Gijangson kalguksu` 🎀)、松亭三代豬肉湯飯 (`Songjeong 3(sam)dae gukbap` 🎀)。")
md.append("3. **南浦洞 (Nampodong) / 札嘎其 (Jagalchi) / 影島 (Yeongdo)**：")
md.append("   - **歷史老字號**：南浦首爾蘿蔔塊牛肉湯 (`Seoul kkakdugi` 🎀)、白火炭烤盲鰻 (`Baekhwa yanggopchang` 🎀)、奶奶蜆湯 (`Halmae jaecheopguk` 🎀🎀)。")
md.append("")
md.append("---")
md.append("")
md.append("## 📊 100家精選餐廳完整總覽表")
md.append("")
md.append("| 編號 | 店名 (英文 / 韓文) | 藍絲帶 (Blue Ribbon) | 飲食種類 | 地址 (可複製韓文至地圖) | 營業時間 / 備註 |")
md.append("| :---: | :--- | :---: | :--- | :--- | :--- |")

for idx in range(len(en_places)):
    e = en_places[idx]
    k = kr_places[idx]
    no = idx + 1
    
    ribbon_cnt = e['ribbon_count']
    if ribbon_cnt == 2:
        ribbon_str = "🎀🎀 **2 個**"
    elif ribbon_cnt == 1:
        ribbon_str = "🎀 **1 個**"
    else:
        ribbon_str = "0 個 (官方推薦)"
        
    name_str = f"**{e['title']}**<br>({k['title_kr']})"
    cuisine_str = f"{e['cuisine']}<br>({k['cuisine_kr']})"
    addr_str = f"{e['address']}<br>`{k['address_kr']}`"
    time_str = e['operating_time'] if e['operating_time'] else "-"
    
    name_str = name_str.replace("|", "/")
    cuisine_str = cuisine_str.replace("|", "/")
    addr_str = addr_str.replace("|", "/")
    time_str = time_str.replace("|", "/")
    
    md.append(f"| {no} | {name_str} | {ribbon_str} | {cuisine_str} | {addr_str} | {time_str} |")

md.append("")
md.append("---")
md.append("")
md.append("## 📖 100家店鋪詳細卡片與官方連結")
md.append("")

for idx in range(len(en_places)):
    e = en_places[idx]
    k = kr_places[idx]
    no = idx + 1
    
    ribbon_cnt = e['ribbon_count']
    ribbon_badge = "🎀" * ribbon_cnt if ribbon_cnt > 0 else "⭐ 釜山百大精選 (0 藍絲帶)"
    ribbon_desc = f"**{ribbon_cnt} 個 Blue Ribbon Survey 藍絲帶**" if ribbon_cnt > 0 else "**0 個** (入選釜山百大精選推薦名單)"
    
    md.append(f"### {no}. {e['title']} ({k['title_kr']})")
    md.append(f"- **獲得幾個Blue Ribbon Survey**：{ribbon_desc} {ribbon_badge}")
    md.append(f"- **店名**：{e['title']} / 韓文：{k['title_kr']}")
    md.append(f"- **飲食種類**：{e['cuisine']} (韓文類別：{k['cuisine_kr']})")
    md.append(f"- **地址**：")
    md.append(f"  - 英文：{e['address']}")
    md.append(f"  - 韓文：`{k['address_kr']}` *(可直接複製至 Naver Map / Kakao Map 導航)*")
    if e['operating_time']:
        md.append(f"- **營業時間**：{e['operating_time']}")
    if e['tag']:
        md.append(f"- **官方推薦主題標籤**：`{e['tag']}`")
    if e['detail_link']:
        md.append(f"- **官方詳細介紹連結**：[Visit Busan 餐廳專頁]({e['detail_link']})")
    md.append("")

with open('FOOD.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print("FOOD.md generated successfully!")
