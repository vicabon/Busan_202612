import json, urllib.parse

with open('visitbusan_100_places.json', 'r', encoding='utf-8') as f:
    en_places = json.load(f)

with open('visitbusan_100_places_kr.json', 'r', encoding='utf-8') as f:
    kr_places = json.load(f)

# Helper function to generate clean Google Maps search query & URL
def make_google_map_url(name_kr, addr_kr):
    # e.g. "톤쇼우 부산 수영구 광안해변로279번길 13"
    # remove building detailed info in parentheses for cleaner search if needed, but keeping road name is best
    clean_addr = addr_kr.split('(')[0].strip() if '(' in addr_kr else addr_kr
    query = f"{name_kr} {clean_addr}"
    return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(query)}"

# 1. Update FOOD.md
two_ribbons = sum(1 for p in en_places if p['ribbon_count'] == 2)
one_ribbon = sum(1 for p in en_places if p['ribbon_count'] == 1)
zero_ribbon = sum(1 for p in en_places if p['ribbon_count'] == 0)

md = []
md.append("# 韓國釜山2026年12月美食指南：Visit Busan 100選 (FOOD.md)")
md.append("")
md.append("> 本文件為 **2026年12月韓國釜山旅遊專案** 之官方精選美食指南，完整收錄 Visit Busan (釜山觀光公社) 評選之 **100 Great Places to Eat in Busan**。")
md.append("> 結合韓國權威美食評鑑 **Blue Ribbon Survey (藍絲帶調查)** 認證標記、中英韓三語對照、**Google Map 導航直達連結**、Naver Map 道路名地址、特色飲食分類與營業時間。")
md.append("")
md.append("---")
md.append("")
md.append("## 📌 藍絲帶調查 (Blue Ribbon Survey) 評級體系說明")
md.append("")
md.append("Blue Ribbon Survey (블루리본 서베이) 創立於2005年，為韓國歷史最悠久、公信力最高的頂級美食評鑑指南：")
md.append(f"- 🎀🎀 **2 個藍絲帶**：在該料理領域具備頂級實力，極力推薦專程造訪（共 **{two_ribbons}** 家）。")
md.append(f"- 🎀 **1 個藍絲帶**：口味卓越、深受在地饕客與旅客喜愛之優質名店（共 **{one_ribbon}** 家）。")
md.append(f"- ⭐ **釜山官方百大精選 (0 個藍絲帶)**：獲釜山觀光公社大力推薦之必吃在地傳統老店或人氣新星（共 **{zero_ribbon}** 家）。")
md.append("")
md.append("---")
md.append("")
md.append("## 📊 100家精選餐廳完整總覽表 (含 Google Map 導航連結)")
md.append("")
md.append("| 編號 | 店名 (英文 / 韓文) | 藍絲帶 | 飲食種類 | 地址與地圖連結 | 營業時間 / 備註 |")
md.append("| :---: | :--- | :---: | :--- | :--- | :--- |")

for idx in range(len(en_places)):
    e = en_places[idx]
    k = kr_places[idx]
    no = idx + 1
    
    ribbon_cnt = e['ribbon_count']
    if ribbon_cnt == 2: ribbon_str = "🎀🎀 **2 個**"
    elif ribbon_cnt == 1: ribbon_str = "🎀 **1 個**"
    else: ribbon_str = "0 個 (官方推薦)"
        
    gmap_url = make_google_map_url(k['title_kr'], k['address_kr'])
    name_str = f"**{e['title']}**<br>({k['title_kr']})"
    cuisine_str = f"{e['cuisine']}<br>({k['cuisine_kr']})"
    addr_str = f"{e['address']}<br>`{k['address_kr']}`<br>[📍 Google Map 導航]({gmap_url})"
    time_str = e['operating_time'] if e['operating_time'] else "-"
    
    name_str = name_str.replace("|", "/")
    cuisine_str = cuisine_str.replace("|", "/")
    addr_str = addr_str.replace("|", "/")
    time_str = time_str.replace("|", "/")
    
    md.append(f"| {no} | {name_str} | {ribbon_str} | {cuisine_str} | {addr_str} | {time_str} |")

md.append("")
md.append("---")
md.append("")
md.append("## 📖 100家店鋪詳細卡片與官方／地圖連結")
md.append("")

for idx in range(len(en_places)):
    e = en_places[idx]
    k = kr_places[idx]
    no = idx + 1
    
    ribbon_cnt = e['ribbon_count']
    ribbon_badge = "🎀" * ribbon_cnt if ribbon_cnt > 0 else "⭐ 釜山百大精選 (0 藍絲帶)"
    ribbon_desc = f"**{ribbon_cnt} 個 Blue Ribbon Survey 藍絲帶**" if ribbon_cnt > 0 else "**0 個** (入選釜山百大精選推薦名單)"
    gmap_url = make_google_map_url(k['title_kr'], k['address_kr'])
    
    md.append(f"### {no}. {e['title']} ({k['title_kr']})")
    md.append(f"- **獲得幾個Blue Ribbon Survey**：{ribbon_desc} {ribbon_badge}")
    md.append(f"- **店名**：{e['title']} / 韓文：{k['title_kr']}")
    md.append(f"- **飲食種類**：{e['cuisine']} (韓文類別：{k['cuisine_kr']})")
    md.append(f"- **地址**：")
    md.append(f"  - 英文：{e['address']}")
    md.append(f"  - 韓文：`{k['address_kr']}` *(可直接複製至 Naver Map / Kakao Map 導航)*")
    md.append(f"- **地圖導航**：[🗺️ 點此開啟 Google Map 查看位置與街景]({gmap_url})")
    if e['operating_time']:
        md.append(f"- **營業時間**：{e['operating_time']}")
    if e['tag']:
        md.append(f"- **官方推薦主題標籤**：`{e['tag']}`")
    if e['detail_link']:
        md.append(f"- **官方詳細介紹連結**：[Visit Busan 餐廳專頁]({e['detail_link']})")
    md.append("")

with open('FOOD.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

# 2. Update BUSAN_100_GREAT_PLACES_TO_EAT.md as well
with open('BUSAN_100_GREAT_PLACES_TO_EAT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print("FOOD.md and BUSAN_100_GREAT_PLACES_TO_EAT.md updated with Google Maps links!")
