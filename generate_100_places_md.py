import json

with open('visitbusan_100_places.json', 'r', encoding='utf-8') as f:
    en_places = json.load(f)

with open('visitbusan_100_places_kr.json', 'r', encoding='utf-8') as f:
    kr_places = json.load(f)

lines = []
lines.append("# Visit Busan 100選美食餐廳 (100 Great Places to Eat in Busan)")
lines.append("")
lines.append("> 資料來源：[Visit Busan 官方網站 (釜山觀光公社)](https://www.visitbusan.net/index.do?menuCd=DOM_000000301002002000)")
lines.append("> 統整日期：2026年9月")
lines.append("> 專案適用：2026年12月韓國釜山自由行美食規劃指南")
lines.append("")
lines.append("本清單完整收錄釜山官方精選之 **100 Great Places to Eat in Busan**，詳細標記每家餐廳之：")
lines.append("1. **獲得幾個 Blue Ribbon Survey (藍絲帶美食調查評級)**")
lines.append("2. **店名 (英文 / 韓文原名)**")
lines.append("3. **地址 (英文地址 / 韓文地址，便於 Naver Map、Kakao Map 導航搜尋)**")
lines.append("4. **飲食種類 (料理類別 / 營業時段 / 特色標籤)**")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 📊 100家精選餐廳總覽表")
lines.append("")
lines.append("| 編號 | 店名 (英文 / 韓文) | 獲得 Blue Ribbon 數 | 飲食種類 | 地址 | 營業時間 / 備註 |")
lines.append("| :---: | :--- | :---: | :--- | :--- | :--- |")

for idx in range(len(en_places)):
    e = en_places[idx]
    k = kr_places[idx]
    
    no = idx + 1
    title_combined = f"**{e['title']}**<br>({k['title_kr']})"
    ribbon_cnt = e['ribbon_count']
    if ribbon_cnt > 0:
        ribbon_str = f"🎀 **{ribbon_cnt} 個**"
    else:
        ribbon_str = "0 個 (入選百大推薦)"
        
    cuisine_combined = f"{e['cuisine']} ({k['cuisine_kr']})"
    addr_combined = f"{e['address']}<br>*(韓: {k['address_kr']})*"
    time_str = e['operating_time'] if e['operating_time'] else "-"
    
    # replace pipe in markdown table
    title_combined = title_combined.replace("|", "\|")
    cuisine_combined = cuisine_combined.replace("|", "/")
    addr_combined = addr_combined.replace("|", "/")
    time_str = time_str.replace("|", "/")
    
    lines.append(f"| {no} | {title_combined} | {ribbon_str} | {cuisine_combined} | {addr_combined} | {time_str} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🍽️ 100家餐廳詳細資料卡 (Detailed Listing)")
lines.append("")

for idx in range(len(en_places)):
    e = en_places[idx]
    k = kr_places[idx]
    no = idx + 1
    
    ribbon_cnt = e['ribbon_count']
    ribbon_badge = "🎀" * ribbon_cnt if ribbon_cnt > 0 else "⭐ 釜山百大精選 (0 藍絲帶)"
    ribbon_desc = f"**{ribbon_cnt} 個 Blue Ribbon Survey 藍絲帶**" if ribbon_cnt > 0 else "**0 個** (入選釜山百大精選推薦名單)"
    
    lines.append(f"### {no}. {e['title']} ({k['title_kr']})")
    lines.append(f"- **獲得幾個Blue Ribbon Survey**：{ribbon_desc} {ribbon_badge}")
    lines.append(f"- **店名**：{e['title']} / 韓文：{k['title_kr']}")
    lines.append(f"- **飲食種類**：{e['cuisine']} (韓文類別：{k['cuisine_kr']})")
    lines.append(f"- **地址**：")
    lines.append(f"  - 英文：{e['address']}")
    lines.append(f"  - 韓文：`{k['address_kr']}` *(可直接複製至 Naver Map / Kakao Map 導航)*")
    if e['operating_time']:
        lines.append(f"- **營業時間**：{e['operating_time']}")
    if e['tag']:
        lines.append(f"- **官方推薦主題標籤**：`{e['tag']}`")
    if e['detail_link']:
        lines.append(f"- **官方詳細介紹連結**：[Visit Busan 餐廳專頁]({e['detail_link']})")
    lines.append("")

output_md = '\n'.join(lines)
with open('BUSAN_100_GREAT_PLACES_TO_EAT.md', 'w', encoding='utf-8') as f:
    f.write(output_md)

print("Created BUSAN_100_GREAT_PLACES_TO_EAT.md successfully!")
