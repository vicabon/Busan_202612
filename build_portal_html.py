import json, urllib.parse

with open('excel_data.json', 'r', encoding='utf-8') as f:
    hotel_data_str = f.read()

with open('visitbusan_100_places.json', 'r', encoding='utf-8') as f:
    en_places = json.load(f)

with open('visitbusan_100_places_kr.json', 'r', encoding='utf-8') as f:
    kr_places = json.load(f)

def make_google_map_url(name_kr, addr_kr):
    clean_addr = addr_kr.split('(')[0].strip() if '(' in addr_kr else addr_kr
    query = f"{name_kr} {clean_addr}"
    return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(query)}"

# Combine food data with Google Maps URLs
food_data = []
for i in range(len(en_places)):
    e = en_places[i]
    k = kr_places[i]
    gmap_link = make_google_map_url(k['title_kr'], k['address_kr'])
    food_data.append({
        'no': i + 1,
        'title_en': e['title'],
        'title_kr': k['title_kr'],
        'ribbon_count': e['ribbon_count'],
        'cuisine_en': e['cuisine'],
        'cuisine_kr': k['cuisine_kr'],
        'address_en': e['address'],
        'address_kr': k['address_kr'],
        'time': e['operating_time'],
        'tag': e['tag'],
        'link': e['detail_link'],
        'gmap_link': gmap_link
    })

food_json_str = json.dumps(food_data, ensure_ascii=False)

# Define 4-Day Itinerary Data Structure
itinerary_data = [
    {
        "day": "Day 1",
        "date": "2026/12/4 (週五)",
        "zone": "東釜山海雲台區",
        "subtitle": "海理團路潮流新店・三麗鷗旗艦店・T1電競朝聖・파도당波浪咖啡・米飛兔與 Club D Oasis 五星海景汗蒸幕",
        "transit": "🚇 地鐵 2 號線「海雲台站 (Haeundae Station)」全程步行串聯，零換乘折返",
        "reason": "✅ 避開 Club D Oasis 週二清潔日提早閉館限制，週五晚間完整暢享海景熱療與戶外足湯！",
        "must_count": 6,
        "events": [
            {
                "time": "10:00 - 11:30",
                "type": "must",
                "badge": "★ 必去指定景點 1",
                "title": "海理團路新店區 (Haeridan-gil / 해리단길)",
                "kr_name": "해리단길",
                "address": "부산 해운대구 우동 518 일대 (海雲台站 4 號出口步行 3 分鐘)",
                "hours": "10:30 - 21:00 (各選物店與咖啡廳略有不同)",
                "desc": "由舊東海南部線鐵道宿舍改建的文青聚落，進駐大量韓國設計師服飾、小眾香氛、復古拍貼機與人氣甜點店。",
                "nearby": "順遊：舊海雲台火車站八角亭建築、鐵道散步公園",
                "food": "☕ 推薦咖啡：Butter Book (奶油書可頌)、Raw & Sweet (精品手沖)",
                "gmap_query": "해리단길 부산 해운대구"
            },
            {
                "time": "11:45 - 13:15",
                "type": "food",
                "badge": "🎀 藍絲帶必吃午餐",
                "title": "海雲台著名母牛排骨 (해운대소문난암소갈비집) 或 錦繡河豚湯 (금수복국)",
                "kr_name": "해운대소문난암소갈비집",
                "address": "부산 해운대구 중동2로10번길 32-10",
                "hours": "11:30 - 22:00 (母牛排骨) / 24小時營業 (錦繡河豚湯)",
                "desc": "【Visit Busan 100選 #14】榮獲 🎀🎀 2個藍絲帶認證！創立於1964年的傳奇韓牛烤排骨，必點生排骨與收尾馬鈴薯粉條；若想喝熱湯則推薦 🎀 1個藍絲帶的錦繡河豚湯。",
                "nearby": "距離龜南路主街步行僅 5 分鐘",
                "food": "🎀🎀 2個藍絲帶：海雲台母牛排骨 ｜ 🎀 1個藍絲帶：錦繡河豚湯 (#35)",
                "gmap_query": "해운대소문난암소갈비집 부산 해운대구 중동2로10번길 32-10"
            },
            {
                "time": "13:30 - 14:20",
                "type": "must",
                "badge": "★ 必去指定景點 2",
                "title": "三麗鷗主題旗艦店（整棟 Sanrio Lovers Club Haeundae）",
                "kr_name": "산리오러버스클럽 해운대",
                "address": "부산 해운대구 구남로 17 (海雲台站 3/5 號出口龜南路主街)",
                "hours": "11:00 - 21:00 (全年無休)",
                "desc": "整棟 1 至 3 樓粉紅色夢幻建築！1 樓為三麗鷗正版限定周邊商品店，2-3 樓為大型主題打卡區與角色造型甜點咖啡廳（Hello Kitty、庫洛米、大耳狗、帕恰狗）。",
                "nearby": "位於海雲台最熱鬧的龜南路文化廣場中心",
                "food": "🍰 店內 2F/3F 角色主題咖啡與造型蛋糕",
                "gmap_query": "산리오러버스클럽 부산 해운대구 구남로 17"
            },
            {
                "time": "14:25 - 15:20",
                "type": "must",
                "badge": "★ 必去指定景點 3",
                "title": "T1 BASE CAMP 釜山店 (티원 베이스캠프 부산)",
                "kr_name": "T1 베이스캠프 부산",
                "address": "부산 해운대구 구남로 37 마리쏠호텔 2층 (距離三麗鷗旗艦店步行僅 2 分鐘！)",
                "hours": "T1 Shop 11:00 - 22:00 ｜ PC Cafe 24小時 ｜ T1 Pub 16:00 - 00:00",
                "desc": "傳奇電競戰隊 T1 (Faker) 官方複合旗艦基地！設有官方隊服與周邊專賣店 (T1 Shop)、高規格電競對戰區、選手榮耀展示牆與觀賽運動酒吧。",
                "nearby": "順遊：海雲台傳統市場（就在轉角處，可順嚐糖餅與魚糕）",
                "food": "🍢 海雲台市場尚國家飯捲、名品糖餅",
                "gmap_query": "T1 베이스캠프 부산 해운대구 구남로 37"
            },
            {
                "time": "15:30 - 16:50",
                "type": "must",
                "badge": "★ 必去指定景點 4",
                "title": "海雲台「波浪」概念咖啡廳：파도당 (Padodang)",
                "kr_name": "파도당 해운대점",
                "address": "부산 해운대구 해운대해변로298번길 24 팔레드시즈 상가 2층 5, 6호",
                "hours": "10:00 - 21:00",
                "desc": "位於海雲台沙灘旁 Pale De CZ 商場 2 樓的海景咖啡廳！超大景觀窗直面海雲台白沙灘與蔚藍大海，招牌為模擬海浪拍岸與沙灘質感的「藍色波浪甜點」與海洋特調。",
                "nearby": "同棟商場內有藍絲帶名店 Mori (모리 懷石料理 🎀 #49)",
                "food": "🌊 必點：파도당 招牌波浪慕斯蛋糕、海鹽奶油拿鐵",
                "gmap_query": "파도당 부산 해운대구 해운대해변로298번길 24"
            },
            {
                "time": "17:00 - 18:00",
                "type": "must",
                "badge": "★ 必去指定景點 5",
                "title": "海雲台 米飛兔（Miffy）專賣店 (미피스토어 부산)",
                "kr_name": "미피스토어 부산",
                "address": "부산 해운대구 달맞이길62번길 21 (尾浦藍線公園旁)",
                "hours": "10:00 - 20:00",
                "desc": "從 파도당 沿著海濱步道往尾浦方向散步 6 分鐘即達！獨家販售釜山限定版「水手服米飛兔」、「海雲台膠囊小火車米飛兔」玩偶、鑰匙圈與生活雜貨。",
                "nearby": "順遊：海雲台藍線公園尾浦站 (Mipo Station，可拍天空膠囊火車進出站海景)",
                "food": "☕ 旁邊亦有 Miffy Cafe 造型雞蛋糕與飲品",
                "gmap_query": "미피스토어 부산 해운대구 달맞이길62번길 21"
            },
            {
                "time": "18:15 - 22:00",
                "type": "must",
                "badge": "★ 必去指定景點 6",
                "title": "Club D Oasis (클럽디오아시스 海雲台 LCT 頂級海景汗蒸幕＆溫泉樂園)",
                "kr_name": "클럽디오아시스",
                "address": "부산 해운대구 달맞이길 30 엘시티 3~6층 (就在米飛兔專賣店正旁邊 LCT 大樓！)",
                "hours": "10:00 - 21:30 / 22:00 (週五晚間完整開放)",
                "desc": "釜山最頂級的五星級海景溫泉複合設施！5 樓擁有面對海雲台大海的戶外無邊際足湯與清水堂露天溫泉，6 樓為五大主題汗蒸幕（鹽房、黃土房、麥飯石、冰房）與海景休息露台。",
                "nearby": "位於 LCT 地標塔內，泡完溫泉下樓即是海雲台夜景步道",
                "food": "🍽️ 晚餐推薦：LCT 內 CHAORAN (차오란 🎀🎀 #42)、巨代炭火烤肉 (거대숯불구이 🎀🎀 #90)",
                "gmap_query": "클럽디오아시스 부산 해운대구 달맞이길 30"
            }
        ]
    },
    {
        "day": "Day 2",
        "date": "2026/12/5 (週六)",
        "zone": "水營灣與廣安里區",
        "subtitle": "Museum 1 光影美術館・釜山電影殿堂・Millac the Market・Podium Dive・BlueLab藥局與週六廣安里無人機秀",
        "transit": "🚇 地鐵 2 號線「Centum City 站」➔「民樂站 / 廣安站」一線直達",
        "reason": "✅ 專程安排於週六造訪廣安里，晚間可免費觀賞週六限定的「廣安里 M 無人機燈光秀 (Drone Show)」！",
        "must_count": 5,
        "events": [
            {
                "time": "10:00 - 11:45",
                "type": "must",
                "badge": "★ 必去指定景點 7",
                "title": "Museum 1 (뮤지엄원 沉浸式光影現代美術館)",
                "kr_name": "뮤지엄원",
                "address": "부산 해운대구 센텀서로 20 (Centum City 站 6 號或 8 號出口步行 5 分鐘)",
                "hours": "平日 10:00 - 19:00 ｜ 週末 10:00 - 20:00 (最後入場為閉館前 1 小時)",
                "desc": "由 8,000 萬顆 LED 燈珠打造地板與四周巨牆的超大型媒體藝術美術館，結合當代藝術家哲學主題展，光影折射極度壯觀好拍。",
                "nearby": "緊鄰 신세계백화점 센텀시티점 (新世界百貨 Centum City 店，金氏世界紀錄最大百貨)",
                "food": "☕ 美術館內設質感咖啡吧，或至新世界百貨地下美食街",
                "gmap_query": "뮤지엄원 부산 해운대구 센텀서로 20"
            },
            {
                "time": "12:00 - 13:30",
                "type": "must",
                "badge": "★ 必去指定景點 8",
                "title": "Centum City 的釜山電影殿堂（BIFF主場地 / 영화의전당）",
                "kr_name": "영화의전당",
                "address": "부산 해운대구 수영강변대로 120 (從 Museum 1 步行約 8 分鐘)",
                "hours": "戶外建築廣場全天開放 ｜ 室內展廳 10:00 - 19:00",
                "desc": "釜山國際電影節 (BIFF) 官方主場館！由奧地利藍天組設計，擁有金氏世界紀錄最長懸臂式屋頂「Big Roof」，解構主義建築線條是建築迷與攝影師必拍聖地。",
                "nearby": "順遊：新世界百貨 Centum City (逛 Gentle Monster, Tamburins, Mardi Mercredi)",
                "food": "🍽️ 附近藍絲帶：AOMORI (아오모리 日料 🎀🎀 #44)、Sushi sian (스시시안 🎀 #78)",
                "gmap_query": "영화의전당 부산 해운대구 수영강변대로 120"
            },
            {
                "time": "13:45 - 15:15",
                "type": "food",
                "badge": "🎀 藍絲帶必吃午餐",
                "title": "Ton shou (톤쇼우 廣安店 — 釜山第一名炭火炸豬排)",
                "kr_name": "톤쇼우 광안점",
                "address": "부산 수영구 광안해변로279번길 13 (민락동)",
                "hours": "11:30 - 21:00 (Last Order 20:00，全年無休)",
                "desc": "【Visit Busan 100選 #1】榮獲 🎀 1個藍絲帶！被譽為全韓國最好吃的炸豬排，使用低溫烹調後經炭火燻烤，推薦必點「Berkshire K 特選里肌炸豬排」，搭配松露鹽與玉米濃湯。",
                "nearby": "距離下一站 Millac the Market 走路僅 2 分鐘！",
                "food": "🎀 備選藍絲帶：Halmae jaecheopguk (할매재첩국 奶奶蜆湯 🎀🎀 #15，就在隔壁條巷子)",
                "gmap_query": "톤쇼우 부산 수영구 광안해변로279번길 13"
            },
            {
                "time": "15:15 - 16:45",
                "type": "must",
                "badge": "★ 必去指定景點 9",
                "title": "Millac the Market (밀락더마켓 民樂水邊複合市集)",
                "kr_name": "밀락더마켓",
                "address": "부산 수영구 민락수변로17번길 56",
                "hours": "10:00 - 24:00 (全年無休)",
                "desc": "榮獲韓國建築大獎的紅磚倉庫改造空間！匯集潮流服飾、文創選物、街頭美食與精釀啤酒，最受歡迎的是面對廣安大橋與遊艇港的巨型大階梯看台。",
                "nearby": "順遊：民樂水邊公園、廣安里海濱長廊",
                "food": "🍺 市集內人氣甜點與精釀啤酒吧",
                "gmap_query": "밀락더마켓 부산 수영구 민락수변로17번길 56"
            },
            {
                "time": "17:00 - 18:30",
                "type": "must",
                "badge": "★ 必去指定景點 10",
                "title": "廣安里複合文化空間：Podium Dive（포디움다이브엠）",
                "kr_name": "포디움다이브엠",
                "address": "부산 수영구 광남로 96 지하 1층~3층 (廣安里海灘旁步行 1 分鐘)",
                "hours": "11:00 - 20:00 (每日營業)",
                "desc": "潛入廣安里地底 B1 至 B3 的沉浸式美學複合空間！結合當代設計策展、黑膠音樂、獨立藝術書店與極簡工業風咖啡廳，是釜山年輕人最新的私房藝術基地。",
                "nearby": "出門走 1 分鐘即是廣安里海水浴場中心沙灘",
                "food": "☕ 館內 Podium Cafe 精品咖啡與烘焙甜點",
                "gmap_query": "포디움다이브엠 부산 수영구 광남로 96"
            },
            {
                "time": "18:40 - 19:40",
                "type": "must",
                "badge": "★ 必去指定景點 11",
                "title": "BlueLab 藥局（블루랩약국 南川海邊旗艦店）",
                "kr_name": "블루랩약국",
                "address": "부산 수영구 남천바다로 38 1~3층 (廣安里海灘南端)",
                "hours": "09:30 - 21:30",
                "desc": "從 Podium Dive 沿廣安里海灘往南走約 6 分鐘即達！1 至 3 樓整棟大型免稅觀光藥局，專營韓國高人氣院線藥妝、修復霜、B群維他命與保健品，現場直接辦理退稅。",
                "nearby": "順遊：南川洞櫻花路與麵包街",
                "food": "🥐 步行3分鐘藍絲帶烘焙：MONSIEUR VINCENT (무슈뱅상 🎀 #11)、Ops 總店 (옵스 🎀 #7)",
                "gmap_query": "블루랩약국 부산 수영구 남천바다로 38"
            },
            {
                "time": "19:45 - 21:30",
                "type": "food",
                "badge": "🎀🎀 藍絲帶晚餐 ＆ 無人機秀",
                "title": "東京飯桌 (동경밥상) 鰻魚飯 / 彥陽烤牛肉 ＆ 週六廣安里 M 無人機燈光秀",
                "kr_name": "동경밥상 / 광안리 M 드론라이트쇼",
                "address": "부산 수영구 남천바다로 34-6 (就在 BlueLab 藥局隔壁兩間店！)",
                "hours": "11:30 - 21:00 (鰻魚飯) ｜ 週六無人機秀 19:00 & 21:00",
                "desc": "BlueLab 藥局正隔壁就是兩間 🎀🎀 2個藍絲帶頂級名店：**東京飯桌 (#81 日式炭烤鰻魚飯三吃)** 與 **彥陽烤牛肉釜山家 (#95 韓牛烤肉)**！晚餐後在廣安里沙灘欣賞數百台無人機在廣安大橋夜空演出的週六限定燈光秀。",
                "nearby": "廣安里海水浴場夜景、廣安大橋燈光秀",
                "food": "🎀🎀 東京飯桌 (#81) ｜ 🎀🎀 彥陽烤牛肉釜山家 (#95)",
                "gmap_query": "동경밥상 부산 수영구 남천바다로 34-6"
            }
        ]
    },
    {
        "day": "Day 3",
        "date": "2026/12/6 (週日)",
        "zone": "中釜山核心與北港區",
        "subtitle": "田浦洞隱密閣樓咖啡 MM’s House・藍絲帶冠軍咖啡巡禮・西面商圈与北港「釜山鯊 (Bukang-i)」傳奇事件現場",
        "transit": "🚇 地鐵 2 號線「田浦站 / 西面站」➔ 地鐵 1 號線「釜山站」",
        "reason": "✅ 避開 MM’s House (므므) 週四公休，於週日午後悠閒品嚐招牌帕芙洛娃，傍晚前往北港親水公園看夕陽與夜景！",
        "must_count": 2,
        "events": [
            {
                "time": "10:30 - 12:00",
                "type": "food",
                "badge": "🎀 藍絲帶必吃早午餐",
                "title": "松亭3代豬肉湯飯 (송정3대국밥) 或 機張手工刀削麵 (기장손칼국수)",
                "kr_name": "송정3대국밥 / 기장손칼국수",
                "address": "부산 부산진구 서면로68번길 33 (西面市場豬肉湯飯街)",
                "hours": "00:00 - 24:00 (松亭3代) / 09:00 - 21:00 (機張刀削麵)",
                "desc": "【Visit Busan 100選 #23 & #98】兩間皆為 🎀 1個藍絲帶認證且相距僅 100 公尺！從 1946 年飄香至今的濃郁豬大骨湯飯，或現擀彈牙的手工刀削麵，開啟元氣滿滿的一天。",
                "nearby": "西面市場、西面地下街",
                "food": "🎀 松亭3代豬肉湯飯 (#23) ｜ 🎀 機張手工刀削麵 (#98)",
                "gmap_query": "송정3대국밥 부산 부산진구 서면로68번길 33"
            },
            {
                "time": "12:15 - 14:15",
                "type": "must",
                "badge": "★ 必去指定景點 12",
                "title": "田浦洞巷弄隱密咖啡廳：MM’s House（Meumeu / 므므）",
                "kr_name": "므므 (MEUMEU)",
                "address": "부산 부산진구 동성로61번길 21-18 2층 (전포동)",
                "hours": "12:00 - 21:00 (週四公休)",
                "desc": "隱身於田浦洞住宅區巷弄二樓的秘密基地咖啡廳！保留老宅木質閣樓的溫馨復古感，招牌必點 **水果蛋白霜帕芙洛娃 (Pavlova / 파블로바)**，酥脆蛋白霜淋上香濃鮮奶油與滿滿當季水果，顏值與美味兼具。",
                "nearby": "順遊：田浦咖啡街 (Jeonpo Cafe Street)、田浦工具街文創小店",
                "food": "🍓 必點：季節水果帕芙洛娃 (Pavlova)、維也納奶油咖啡",
                "gmap_query": "므므 부산 부산진구 동성로61번길 21-18"
            },
            {
                "time": "14:15 - 16:00",
                "type": "food",
                "badge": "🎀🎀 藍絲帶精品咖啡＆選物巡禮",
                "title": "田浦＆西面 三大 2個藍絲帶咖啡名店 ＆ 西面商圈逛街",
                "kr_name": "히떼로스터리 / 블랙업커피 / 베르크로스터스",
                "address": "부산 부산진구 동성로 59 (HYTTE ROASTERY，就在 므므 隔壁條街！)",
                "hours": "10:00 - 22:00",
                "desc": "田浦洞是全釜山藍絲帶咖啡廳密度最高的地方！從 므므 步行 2 分鐘即可抵達 **HYTTE ROASTERY (#3 🎀🎀)**；往西面方向走則有以「海鹽咖啡」聞名的 **BLACKUP COFFEE (#4 🎀🎀)** 與自家烘焙名店 **Werk Roasters (#5 🎀🎀)**。",
                "nearby": "順遊：NC百貨位置商圈、KT&G 想像空間 (Sangsang Madang Busan 設計大樓)",
                "food": "🎀🎀 HYTTE ROASTERY (#3) ｜ 🎀🎀 BLACKUP COFFEE (#4) ｜ 🎀🎀 Werk Roasters (#5)",
                "gmap_query": "히떼로스터리 부산 부산진구 동성로 59"
            },
            {
                "time": "16:20 - 18:30",
                "type": "must",
                "badge": "★ 必去指定景點 13",
                "title": "北港「釜山鯊」事件現場（Bukang-i / 부캉이・北港親水公園人工水路）",
                "kr_name": "부산북항친수공원 (부캉이 출몰지)",
                "address": "부산 동구 충장대로 206 (地鐵釜山站透過空中連通道步行約 10 分鐘)",
                "hours": "06:00 - 23:00 (公園全區免費開放)",
                "desc": "轟動全韓國的 2026 年傳奇事件現場！一隻長達 3 公尺的大型鯊魚游入北港親水公園人工生態水路並定居超過一個月，被網友取名為 **「부캉이 (Bukang-i)」** 甚至獲頒釜山名譽宣傳大使，吸引數十萬遊客前來水路橋邊打卡朝聖！傍晚時分更可同時飽覽釜山港大橋與北港歌劇院絕美夕陽與夜景。",
                "nearby": "順遊：釜山站空中景觀廣場、草梁故事路 (168階梯單軌電車)",
                "food": "☕ 公園周邊海景咖啡車或草梁牛奶咖啡廳",
                "gmap_query": "부산북항친수공원 부산 동구 충장대로 206"
            },
            {
                "time": "18:45 - 20:30",
                "type": "food",
                "badge": "🎀 藍絲帶必吃晚餐",
                "title": "釜山站草梁＆上海街藍絲帶名店：新發園 / 平山屋 / 銀河排骨",
                "kr_name": "신발원 / 평산옥 / 은하갈비",
                "address": "부산 동구 대영로243번길 62 (新發園，釜山站對面上海街)",
                "hours": "11:00 - 21:00",
                "desc": "從北港親水公園走回釜山站對面，即聚集三間 Visit Busan 100選藍絲帶老店：**新發園 (#22 🎀 爆汁鮮肉大餃子與糖醋肉)**、**平山屋 (#16 🎀 百年白切豬肉片配涼拌麵)**、**銀河排骨 (#100 🎀 傳統炭烤調味豬排骨)**。",
                "nearby": "釜山站上海街牌樓夜景",
                "food": "🎀 新發園 (#22) ｜ 🎀 平山屋 (#16) ｜ 🎀 銀河排骨 (#100)",
                "gmap_query": "신발원 부산 동구 대영로243번길 62"
            }
        ]
    },
    {
        "day": "Day 4",
        "date": "2026/12/7 (週一)",
        "zone": "西釜山老城與影島區",
        "subtitle": "甘川洞法國授權小王子之家・影島 ARTE MUSEUM 世界最大光影館・南浦洞最大 Olive Young 與伴手禮狂歡",
        "transit": "🚇 地鐵 1 號線「土城站 (甘川洞)」➔ 過橋至「影島」➔「南浦站 (光復路商圈)」",
        "reason": "✅ 最後一個完整旅遊日安排於南浦洞最大 Olive Young 旗艦店與免稅藥局收尾，買完直接回飯店打包行李最輕鬆！",
        "must_count": 3,
        "events": [
            {
                "time": "09:30 - 12:00",
                "type": "must",
                "badge": "★ 必去指定景點 14",
                "title": "法國正式授權的小王子之家（甘川洞新拍照點 / Little Prince House）",
                "kr_name": "리틀프린스 하우스 (감천문화마을)",
                "address": "부산 사하구 감내1로 200 (甘川洞文化村入口處原甘內交流中心大樓)",
                "hours": "09:30 - 18:30 (每日營業)",
                "desc": "由法國聖修伯里遺產管理委員會正式官方授權！整棟多樓層沉浸式小王子主題館，打造 B612 星球玫瑰花園、狐狸秘境、飛行員畫室等夢幻室內場景，頂樓觀景台更可無遮蔽俯瞰甘川洞彩色階梯屋頂與大海，不用再排隊苦等戶外欄杆！",
                "nearby": "順遊：甘川洞文化村主街、小王子與沙漠狐狸戶外雕像、手翻書製作體驗",
                "food": "☕ 館內小王子主題咖啡廳、甘川洞糖餅與雲朵拿鐵",
                "gmap_query": "리틀프린스 하우스 부산 사하구 감내1로 200"
            },
            {
                "time": "12:30 - 14:00",
                "type": "food",
                "badge": "🎀🎀 藍絲帶海景午餐",
                "title": "影島 牧場園 (목장원 韓牛烤肉) 或 白淺灘文化村海景餐酒館",
                "kr_name": "목장원",
                "address": "부산 영도구 절영로 355 (동삼동)",
                "hours": "11:30 - 21:30",
                "desc": "【Visit Busan 100選 #57】榮獲 🎀🎀 2個藍絲帶！位於影島絕影海岸路旁的大型海景莊園餐廳，一邊品嚐頂級韓牛排骨或韓式定食，一邊眺望南港大橋與蔚藍海岸。",
                "nearby": "順遊：白淺灘文化村 (Huinnyeoul Culture Village) 海岸絕壁步道",
                "food": "🎀🎀 牧場園 (#57) ｜ ☕ 白淺灘海景咖啡廳 Aether / Having Moment",
                "gmap_query": "목장원 부산 영도구 절영로 355"
            },
            {
                "time": "14:15 - 16:45",
                "type": "must",
                "badge": "★ 必去指定景點 15",
                "title": "ARTE MUSEUM 影島（아르떼뮤지엄 부산 世界最大規模沉浸式美術館）",
                "kr_name": "아르떼뮤지엄 부산",
                "address": "부산 영도구 해양로247번길 29 (동삼동)",
                "hours": "10:00 - 20:00 (最後入場 19:00，全年無休)",
                "desc": "全球最大規模的 ARTE MUSEUM 釜山館！由 d'strict 團隊打造，以「CIRCLE (循環)」為題展出 19 個超巨型數位光影作品（包含釜山專屬璀璨海浪、龍捲風、無限花海、太陽與法國奧賽美術館聯名展區），五感震撼無與倫比。",
                "nearby": "正隔壁步行 1 分鐘即是 P.ARK (피아크) 巨型郵輪造型海景複合文化咖啡廳",
                "food": "🍵 館內 ARTE TEA BAR 光影互動茶飲 ｜ 🥐 P.ARK 景觀烘焙咖啡廳",
                "gmap_query": "아르떼뮤지엄 부산 영도구 해양로247번길 29"
            },
            {
                "time": "17:15 - 19:30",
                "type": "must",
                "badge": "★ 必去指定景點 16",
                "title": "釜山最大 Olive Young 南浦 Town（올리브영 남포타운）＆ 南浦免稅藥局",
                "kr_name": "올리브영 남포타운",
                "address": "부산 중구 광복로 64-1 (地鐵南浦站 1 號或 3 號出口光復路主街)",
                "hours": "10:00 - 22:30",
                "desc": "整棟 1 至 4 樓、全釜山規模最大的 Olive Young 旗艦店！貨源最齊全，設有 AI 肌膚檢測體驗吧、K-Beauty 彩妝專區、零食貝果片與外國人即時退稅櫃台。逛完還可順道在光復路與 BIFF 廣場旁的大型免稅藥局（如 부산 레디영 약국、남포온누리약국）最後補貨。",
                "nearby": "順遊：BIFF 廣場（吃黑糖堅果糖餅）、光復路冬季聖誕樹燈飾街、國際市場、札嘎其市場",
                "food": "🥖 旁邊即是藍絲帶麵包名店 B&C (비엔씨 광복점 🎀 #26)",
                "gmap_query": "올리브영 남포타운 부산 중구 광복로 64-1"
            },
            {
                "time": "19:30 - 21:30",
                "type": "food",
                "badge": "🎀 藍絲帶壓軸晚餐",
                "title": "李在模披薩 (이재모피자) 或 首爾蘿蔔塊雪濃湯 (서울깍두기) / 新昌湯飯",
                "kr_name": "이재모피자 / 서울깍두기",
                "address": "부산 중구 광복중앙로 31 (李在模披薩，就在 Olive Young 南浦 Town 步行 3 分鐘處)",
                "hours": "10:00 - 21:10 (李在模披薩，週日公休，故排在週一最完美！)",
                "desc": "【Visit Busan 100選 #69 & #24】特別將南浦洞排在週一，正是為了避開 **李在模披薩 (#69 🎀)** 的週日公休！品嚐牽絲爆量的韓國任實起司邊烤披薩；或享用 **首爾蘿蔔塊 (#24 🎀)** 濃郁韓牛雪濃湯，為四天釜山之旅畫下完美句點。",
                "nearby": "龍頭山公園釜山塔夜景",
                "food": "🎀 李在模披薩 (#69) ｜ 🎀 首爾蘿蔔塊 (#24) ｜ 🎀 新昌湯飯 (#21)",
                "gmap_query": "이재모피자 부산 중구 광복중앙로 31"
            }
        ]
    }
]

for d in itinerary_data:
    for ev in d['events']:
        ev['gmap_url'] = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(ev['gmap_query'])}"

itinerary_json_str = json.dumps(itinerary_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2026年12月 韓國釜山旅遊指南：行程 (Itinerary) ・ 住 (Hotel) ・ 食 (Food 100選)</title>
  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-light: #2563eb;
      --food-primary: #b91c1c;
      --food-light: #dc2626;
      --itin-primary: #0f766e;
      --itin-light: #0d9488;
      --accent: #e11d48;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --text: #0f172a;
      --text-muted: #64748b;
      --highlight-bg: #fff1f2;
      --highlight-text: #be123c;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft JhengHei", sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.55;
      padding-bottom: 60px;
    }}

    /* Global Header */
    header {{
      background: linear-gradient(135deg, #091325 0%, #0f766e 48%, #1e3a8a 100%);
      color: white;
      padding: 28px 20px 22px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.14);
    }}
    header h1 {{ font-size: 1.85rem; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.5px; }}
    header p {{ font-size: 0.95rem; color: #cbd5e1; max-width: 920px; margin: 0 auto; }}

    /* Main Category Toggle: 行程 (Itinerary) vs 住 (Hotel) vs 食 (Food) */
    .main-nav-wrapper {{
      max-width: 980px;
      margin: 18px auto 0;
      display: flex;
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(8px);
      padding: 5px;
      border-radius: 9999px;
      border: 1px solid rgba(255,255,255,0.25);
      gap: 4px;
    }}
    .main-nav-btn {{
      flex: 1;
      padding: 10px 16px;
      border: none;
      background: transparent;
      color: #e2e8f0;
      font-size: 1.0rem;
      font-weight: 700;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      white-space: nowrap;
    }}
    .main-nav-btn.active.itin {{
      background: #0f766e;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.28);
    }}
    .main-nav-btn.active.hotel {{
      background: #1e3a8a;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.28);
    }}
    .main-nav-btn.active.food {{
      background: #b91c1c;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.28);
    }}

    .container {{
      max-width: 1440px;
      margin: 20px auto;
      padding: 0 16px;
    }}

    /* Sub-tabs Navigation */
    .subtabs-wrapper {{
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--bg);
      padding: 10px 0;
    }}
    .subtabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      -webkit-overflow-scrolling: touch;
    }}
    .subtabs::-webkit-scrollbar {{ height: 4px; }}
    .subtabs::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 4px; }}
    
    .tab-btn {{
      padding: 9px 16px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .tab-btn:hover {{ background: #f1f5f9; color: var(--text); }}
    .tab-btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
      box-shadow: 0 4px 10px rgba(30, 58, 138, 0.2);
    }}
    .tab-btn.active.food-filter {{
      background: var(--food-primary);
      border-color: var(--food-primary);
      box-shadow: 0 4px 10px rgba(185, 28, 28, 0.2);
    }}
    .tab-btn.active.itin-filter {{
      background: var(--itin-primary);
      border-color: var(--itin-primary);
      box-shadow: 0 4px 10px rgba(15, 118, 110, 0.22);
    }}

    /* Control Bar */
    .control-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin: 14px 0;
      background: var(--card-bg);
      padding: 12px 16px;
      border-radius: 10px;
      border: 1px solid var(--border);
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      align-items: center;
    }}
    .search-input {{
      flex: 1;
      min-width: 240px;
      padding: 9px 14px;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.95rem;
      outline: none;
      transition: border 0.2s;
    }}
    .search-input:focus {{ border-color: var(--primary-light); }}
    .search-input.food-focus:focus {{ border-color: var(--food-light); }}
    .stats-badge {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-left: auto;
    }}

    /* Frozen Table Container */
    .table-container {{
      background: var(--card-bg);
      border-radius: 10px;
      border: 1px solid var(--border);
      overflow-x: auto;
      overflow-y: auto;
      max-height: 75vh;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      display: block;
      position: relative;
    }}
    .table-container::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    .table-container::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 4px; }}
    table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      text-align: left;
      font-size: 0.88rem;
    }}
    th {{
      background: #f1f5f9;
      color: #1e293b;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 2px solid #cbd5e1;
      border-right: 1px solid #e2e8f0;
      white-space: nowrap;
      position: sticky;
      top: 0;
      z-index: 20;
      cursor: pointer;
      user-select: none;
      transition: background 0.15s ease;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    th:hover {{ background: #e2e8f0; color: #0f172a; }}
    th.sorted-asc, th.sorted-desc {{ background: #e0e7ff; color: #1e3a8a; border-bottom-color: #3b82f6; }}
    .sort-icon {{ display: inline-block; margin-left: 6px; font-size: 0.85rem; opacity: 0.5; }}
    th.sorted-asc .sort-icon, th.sorted-desc .sort-icon {{ opacity: 1; color: #1d4ed8; font-weight: 900; }}
    th.food-th {{ background: #fef2f2; color: #991b1b; }}
    th.food-th:hover {{ background: #fee2e2; }}
    th.food-th.sorted-asc, th.food-th.sorted-desc {{ background: #ffe4e6; color: #9f1239; }}

    td {{
      padding: 11px 14px;
      border-bottom: 1px solid var(--border);
      border-right: 1px solid #f1f5f9;
      vertical-align: middle;
    }}
    tr:hover td {{ background-color: #f8fafc; }}
    tr:nth-child(even) td {{ background-color: #fafafa; }}

    /* Mobile Cards View */
    .cards-container {{
      display: none;
      flex-direction: column;
      gap: 14px;
    }}
    .item-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }}
    .card-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
      margin-bottom: 10px;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 10px;
    }}
    .card-title {{ font-size: 1.05rem; font-weight: 700; color: var(--text); }}
    .card-star {{
      background: #fef3c7;
      color: #b45309;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      white-space: nowrap;
    }}
    .card-row {{ display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 0.85rem; }}
    .card-label {{ color: var(--text-muted); font-weight: 500; min-width: 90px; }}
    .card-val {{ font-weight: 600; text-align: right; word-break: break-word; }}

    /* Badges & Buttons */
    .gmap-btn {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: #f0fdf4;
      color: #15803d;
      border: 1px solid #bbf7d0;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.82rem;
      text-decoration: none;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .gmap-btn:hover {{
      background: #22c55e;
      color: white;
      border-color: #22c55e;
      box-shadow: 0 2px 8px rgba(34, 197, 94, 0.3);
    }}
    .ribbon-pill {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.82rem;
      white-space: nowrap;
    }}
    .ribbon-pill.two {{ background: #fdf2f8; color: #be185d; border-color: #fbcfe8; }}
    .weighted-badge {{
      display: inline-block;
      background: var(--highlight-bg);
      color: var(--highlight-text);
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.83rem;
      border: 1px solid #fecdd3;
    }}
    .score-badge {{
      display: inline-block;
      background: #f0fdf4;
      color: #166534;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 0.83rem;
    }}
    .price-text {{ color: #0369a1; font-weight: 700; }}
    .addr-copy {{
      font-family: Consolas, monospace;
      background: #f1f5f9;
      padding: 2px 6px;
      border-radius: 4px;
      color: #334155;
      font-size: 0.8rem;
    }}
    .tag-badge {{
      display: inline-block;
      background: #f1f5f9;
      color: #475569;
      font-size: 0.75rem;
      padding: 2px 6px;
      border-radius: 4px;
      margin-top: 4px;
    }}

    /* ITINERARY SECTION STYLES */
    .itin-summary-banner {{
      background: linear-gradient(135deg, #f0fdfa 0%, #e0f2fe 100%);
      border: 1px solid #99f6e4;
      border-radius: 12px;
      padding: 18px 22px;
      margin-bottom: 20px;
      box-shadow: 0 2px 6px rgba(15, 118, 110, 0.06);
    }}
    .itin-summary-banner h2 {{
      font-size: 1.15rem;
      color: #0f766e;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .checklist-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 8px;
      margin-top: 12px;
    }}
    .check-item {{
      background: rgba(255,255,255,0.85);
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 6px 10px;
      font-size: 0.83rem;
      font-weight: 600;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .check-item span.day-tag {{
      background: #0f766e;
      color: white;
      font-size: 0.72rem;
      padding: 1px 6px;
      border-radius: 4px;
      margin-left: auto;
      white-space: nowrap;
    }}

    .day-block {{
      background: var(--card-bg);
      border-radius: 14px;
      border: 1px solid var(--border);
      margin-bottom: 28px;
      overflow: hidden;
      box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    }}
    .day-header {{
      background: linear-gradient(135deg, #0f766e 0%, #1e3a8a 100%);
      color: white;
      padding: 18px 24px;
    }}
    .day-header-top {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }}
    .day-title {{ font-size: 1.35rem; font-weight: 800; }}
    .day-zone-badge {{
      background: rgba(255,255,255,0.2);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
    }}
    .day-subtitle {{ font-size: 0.95rem; color: #e2e8f0; margin-bottom: 8px; }}
    .day-meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.83rem;
      background: rgba(0,0,0,0.2);
      padding: 8px 12px;
      border-radius: 8px;
      color: #f8fafc;
    }}

    /* Timeline Events */
    .timeline {{
      padding: 20px 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .timeline-card {{
      border: 1px solid var(--border);
      border-left: 5px solid #0f766e;
      border-radius: 10px;
      padding: 16px 18px;
      background: #ffffff;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}
    .timeline-card.food-type {{
      border-left-color: #e11d48;
      background: #fffafa;
    }}
    .timeline-card:hover {{
      box-shadow: 0 4px 12px rgba(0,0,0,0.07);
    }}
    .tl-top {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .tl-time {{
      font-family: Consolas, monospace;
      font-weight: 800;
      font-size: 0.92rem;
      color: #0f766e;
      background: #ccfbf1;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    .timeline-card.food-type .tl-time {{
      color: #be123c;
      background: #ffe4e6;
    }}
    .tl-badge {{
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 6px;
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde68a;
    }}
    .timeline-card.food-type .tl-badge {{
      background: #fce7f3;
      color: #be185d;
      border-color: #fbcfe8;
    }}
    .tl-title {{
      font-size: 1.12rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 6px;
    }}
    .tl-desc {{
      font-size: 0.92rem;
      color: #334155;
      margin-bottom: 10px;
    }}
    .tl-info-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 8px;
      background: #f8fafc;
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      font-size: 0.84rem;
    }}
    .tl-info-item {{
      display: flex;
      align-items: flex-start;
      gap: 6px;
    }}
    .tl-info-label {{
      font-weight: 700;
      color: #475569;
      white-space: nowrap;
    }}

    @media (max-width: 900px) {{
      .table-container {{ display: none; }}
      .cards-container {{ display: flex; }}
      header h1 {{ font-size: 1.35rem; }}
      .main-nav-btn {{ font-size: 0.85rem; padding: 9px 10px; }}
      .control-bar {{ padding: 10px; }}
      .tab-btn {{ padding: 8px 12px; font-size: 0.82rem; }}
      .timeline {{ padding: 14px; }}
      .day-header {{ padding: 14px 16px; }}
      .day-title {{ font-size: 1.15rem; }}
    }}
  </style>
</head>
<body>

  <header>
    <h1>🇰🇷 2026年12月 韓國釜山自由行全方位指南</h1>
    <p>旅遊日期：2026/12/3 ~ 12/8（實際完整遊玩 4 天：12/4 ~ 12/7）｜ 16大必去景點分區行程 ・ 住宿大數據評比 ・ Visit Busan 100選美食</p>
    
    <!-- Main 3-Way Tab Selector -->
    <div class="main-nav-wrapper">
      <button class="main-nav-btn active itin" id="mainTabItin" onclick="switchMainSection('itin')">
        🗓️ 4日分區行程 (12/4-12/7)
      </button>
      <button class="main-nav-btn hotel" id="mainTabHotel" onclick="switchMainSection('hotel')">
        🏨 住宿評比 (Hotel)
      </button>
      <button class="main-nav-btn food" id="mainTabFood" onclick="switchMainSection('food')">
        🍽️ 釜山100選美食 (Food)
      </button>
    </div>
  </header>

  <div class="container">

    <!-- SECTION 0: 4-DAY ITINERARY (12/4 - 12/7) -->
    <div id="itinSection">
      <div class="subtabs-wrapper">
        <div class="subtabs" id="itinSubtabs">
          <button class="tab-btn active itin-filter" onclick="filterItineraryDay('ALL', this)">🗺️ 4天完整行程總覽 (12/4 ~ 12/7)</button>
          <button class="tab-btn" onclick="filterItineraryDay('Day 1', this)">Day 1：12/4 (五) 東釜山海雲台區</button>
          <button class="tab-btn" onclick="filterItineraryDay('Day 2', this)">Day 2：12/5 (六) 廣安里＆水營灣區</button>
          <button class="tab-btn" onclick="filterItineraryDay('Day 3', this)">Day 3：12/6 (日) 西面田浦＆北港區</button>
          <button class="tab-btn" onclick="filterItineraryDay('Day 4', this)">Day 4：12/7 (一) 甘川洞・影島・南浦洞</button>
        </div>
      </div>

      <!-- 16 Must-Visit Spots Checklist Banner -->
      <div class="itin-summary-banner">
        <h2>✅ 您指定的 16 大必去景點：已 100% 依區域與營業時間完美排入 12/4 ~ 12/7！</h2>
        <p style="font-size: 0.88rem; color: #334155;">
          <strong>分區不折返原則</strong>：每天鎖定單一生活圈，結合營業日檢查（避開 Club D Oasis 週二提早閉館、避開 MM's House 週四公休、避開李在模披薩週日公休，並鎖定週六晚間廣安里無人機秀）。
        </p>
        <div class="checklist-grid">
          <div class="check-item">1. 海理團路新店區 <span class="day-tag">12/4 Day 1</span></div>
          <div class="check-item">2. 三麗鷗主題旗艦店(整棟) <span class="day-tag">12/4 Day 1</span></div>
          <div class="check-item">3. T1 BASE CAMP 釜山店 <span class="day-tag">12/4 Day 1</span></div>
          <div class="check-item">4. 波浪概念咖啡：파도당 <span class="day-tag">12/4 Day 1</span></div>
          <div class="check-item">5. 海雲台 米飛兔專賣店 <span class="day-tag">12/4 Day 1</span></div>
          <div class="check-item">6. Club D Oasis 海景汗蒸幕 <span class="day-tag">12/4 Day 1</span></div>
          <div class="check-item">7. Museum 1 光影美術館 <span class="day-tag">12/5 Day 2</span></div>
          <div class="check-item">8. Centum 釜山電影殿堂 <span class="day-tag">12/5 Day 2</span></div>
          <div class="check-item">9. Millac the Market <span class="day-tag">12/5 Day 2</span></div>
          <div class="check-item">10. 廣安里 Podium Dive <span class="day-tag">12/5 Day 2</span></div>
          <div class="check-item">11. BlueLab 藥局 <span class="day-tag">12/5 Day 2</span></div>
          <div class="check-item">12. 田浦洞 MM’s House (므므) <span class="day-tag">12/6 Day 3</span></div>
          <div class="check-item">13. 北港「釜山鯊 (부캉이)」現場 <span class="day-tag">12/6 Day 3</span></div>
          <div class="check-item">14. 甘川洞法國授權小王子之家 <span class="day-tag">12/7 Day 4</span></div>
          <div class="check-item">15. ARTE MUSEUM 影島 <span class="day-tag">12/7 Day 4</span></div>
          <div class="check-item">16. 釜山最大 Olive Young 南浦 <span class="day-tag">12/7 Day 4</span></div>
        </div>
      </div>

      <!-- Dynamic Itinerary Container -->
      <div id="itineraryContainer"></div>
    </div>
    
    <!-- SECTION 1: HOTEL -->
    <div id="hotelSection" style="display: none;">
      <div class="subtabs-wrapper">
        <div class="subtabs" id="hotelSubtabs"></div>
      </div>

      <div class="control-bar">
        <input type="text" id="hotelSearchInput" class="search-input" placeholder="🔍 搜尋飯店名稱、星級、位置、價格或關鍵字..." oninput="renderHotelSheet()">
        <div class="stats-badge" id="hotelStatsBadge">載入中...</div>
      </div>

      <div class="table-container">
        <table id="hotelTable">
          <thead id="hotelTableHead"></thead>
          <tbody id="hotelTableBody"></tbody>
        </table>
      </div>

      <div class="cards-container" id="hotelCardsContainer"></div>
    </div>

    <!-- SECTION 2: FOOD -->
    <div id="foodSection" style="display: none;">
      <div class="subtabs-wrapper">
        <div class="subtabs" id="foodSubtabs">
          <button class="tab-btn active food-filter" onclick="filterFoodRibbon('ALL', this)">🌟 全部 100 家餐廳</button>
          <button class="tab-btn" onclick="filterFoodRibbon('2', this)">🎀🎀 2個藍絲帶 (Top Gourmet)</button>
          <button class="tab-btn" onclick="filterFoodRibbon('1', this)">🎀 1個藍絲帶 (Recommended)</button>
          <button class="tab-btn" onclick="filterFoodRibbon('0', this)">⭐ 官方百大推薦 (Local Picks)</button>
        </div>
      </div>

      <div class="control-bar">
        <input type="text" id="foodSearchInput" class="search-input food-focus" placeholder="🔍 搜尋店名(中英韓)、料理種類(豬肉湯飯/烤肉/炸豬排/咖啡)、行政區或地址..." oninput="renderFoodList()">
        <div class="stats-badge" id="foodStatsBadge">載入中...</div>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th class="food-th" style="width: 50px; text-align: center;" onclick="sortFood('no')">No. <span class="sort-icon" id="food_sort_no">⇅</span></th>
              <th class="food-th" onclick="sortFood('title_en')">店名 (英文 / 韓文) <span class="sort-icon" id="food_sort_title_en">⇅</span></th>
              <th class="food-th" onclick="sortFood('ribbon_count')">Blue Ribbon 評級 <span class="sort-icon" id="food_sort_ribbon_count">⇅</span></th>
              <th class="food-th" onclick="sortFood('cuisine_en')">料理種類 <span class="sort-icon" id="food_sort_cuisine_en">⇅</span></th>
              <th class="food-th">地址 (可複製韓文導航)</th>
              <th class="food-th" style="text-align: center;">Google Map 導航</th>
              <th class="food-th">營業時間與主題</th>
            </tr>
          </thead>
          <tbody id="foodTableBody"></tbody>
        </table>
      </div>

      <div class="cards-container" id="foodCardsContainer"></div>
    </div>

  </div>

  <script>
    const HOTEL_EXCEL_DATA = {hotel_data_str};
    const FOOD_DATA = {food_json_str};
    const ITINERARY_DATA = {itinerary_json_str};

    let currentMainSection = "itin";
    let currentItineraryFilter = "ALL";
    let currentHotelSheet = "綜合總結比價 (Summary)";
    let currentFoodRibbonFilter = "ALL";

    // Sorting states
    let hotelSortCol = null;
    let hotelSortDir = "asc";

    let foodSortCol = null;
    let foodSortDir = "asc";

    const hotelTabs = [
      {{ name: "綜合總結比價 (Summary)", label: "綜合比價與加權總評", icon: "⭐" }},
      {{ name: "Agoda.com", label: "Agoda.com", icon: "🔴" }},
      {{ name: "Booking.com", label: "Booking.com", icon: "🔵" }},
      {{ name: "Trip.com", label: "Trip.com", icon: "🌐" }},
      {{ name: "Tripadvisor.com", label: "Tripadvisor", icon: "🟢" }},
      {{ name: "Google Map", label: "Google Map", icon: "🟠" }}
    ];

    function switchMainSection(sec) {{
      currentMainSection = sec;
      const itinBtn = document.getElementById("mainTabItin");
      const hotelBtn = document.getElementById("mainTabHotel");
      const foodBtn = document.getElementById("mainTabFood");

      const itinSec = document.getElementById("itinSection");
      const hotelSec = document.getElementById("hotelSection");
      const foodSec = document.getElementById("foodSection");

      itinBtn.className = "main-nav-btn itin";
      hotelBtn.className = "main-nav-btn hotel";
      foodBtn.className = "main-nav-btn food";

      itinSec.style.display = "none";
      hotelSec.style.display = "none";
      foodSec.style.display = "none";

      if (sec === "itin") {{
        itinBtn.className = "main-nav-btn active itin";
        itinSec.style.display = "block";
        renderItinerary();
      }} else if (sec === "hotel") {{
        hotelBtn.className = "main-nav-btn active hotel";
        hotelSec.style.display = "block";
        renderHotelSheet();
      }} else {{
        foodBtn.className = "main-nav-btn active food";
        foodSec.style.display = "block";
        renderFoodList();
      }}
    }}

    // Itinerary logic
    function filterItineraryDay(dayVal, btnEl) {{
      currentItineraryFilter = dayVal;
      const btns = document.querySelectorAll("#itinSubtabs .tab-btn");
      btns.forEach(b => b.className = "tab-btn");
      btnEl.className = "tab-btn active itin-filter";
      renderItinerary();
    }}

    function renderItinerary() {{
      const container = document.getElementById("itineraryContainer");
      const days = ITINERARY_DATA.filter(d => currentItineraryFilter === "ALL" || d.day === currentItineraryFilter);

      container.innerHTML = days.map(d => {{
        const eventsHtml = d.events.map(ev => {{
          const cardCls = ev.type === "food" ? "timeline-card food-type" : "timeline-card";
          return `
            <div class="${{cardCls}}">
              <div class="tl-top">
                <span class="tl-time">🕒 ${{ev.time}}</span>
                <span class="tl-badge">${{ev.badge}}</span>
                <a href="${{ev.gmap_url}}" target="_blank" rel="noopener noreferrer" class="gmap-btn" style="margin-left: auto;">
                  📍 Google Map 導航
                </a>
              </div>
              <div class="tl-title">${{ev.title}}</div>
              <div class="tl-desc">${{ev.desc}}</div>
              <div class="tl-info-grid">
                <div class="tl-info-item">
                  <span class="tl-info-label">📍 韓文地址：</span>
                  <span class="addr-copy">${{ev.address}}</span>
                </div>
                <div class="tl-info-item">
                  <span class="tl-info-label">⏰ 營業時間：</span>
                  <span>${{ev.hours}}</span>
                </div>
                <div class="tl-info-item">
                  <span class="tl-info-label">👣 順遊亮點：</span>
                  <span>${{ev.nearby}}</span>
                </div>
                <div class="tl-info-item">
                  <span class="tl-info-label">🍽️ 美食推薦：</span>
                  <span style="color: #be123c; font-weight: 600;">${{ev.food}}</span>
                </div>
              </div>
            </div>
          `;
        }}).join("");

        return `
          <div class="day-block">
            <div class="day-header">
              <div class="day-header-top">
                <div class="day-title">${{d.day}} ｜ ${{d.date}} — 【${{d.zone}}】</div>
                <div class="day-zone-badge">包含 ${{d.must_count}} 個必去指定景點</div>
              </div>
              <div class="day-subtitle">${{d.subtitle}}</div>
              <div class="day-meta-bar">
                <span>${{d.transit}}</span>
                <span>｜</span>
                <span>${{d.reason}}</span>
              </div>
            </div>
            <div class="timeline">
              ${{eventsHtml}}
            </div>
          </div>
        `;
      }}).join("");
    }}

    // Hotel subtabs
    function initHotelSubtabs() {{
      const c = document.getElementById("hotelSubtabs");
      c.innerHTML = "";
      hotelTabs.forEach(t => {{
        const btn = document.createElement("button");
        btn.className = `tab-btn ${{t.name === currentHotelSheet ? "active" : ""}}`;
        btn.innerHTML = `${{t.icon}} ${{t.label}}`;
        btn.onclick = () => {{
          currentHotelSheet = t.name;
          hotelSortCol = null;
          initHotelSubtabs();
          document.getElementById("hotelSearchInput").value = "";
          renderHotelSheet();
        }};
        c.appendChild(btn);
      }});
    }}

    function sortHotel(headerName) {{
      if (hotelSortCol === headerName) {{
        hotelSortDir = hotelSortDir === "asc" ? "desc" : "asc";
      }} else {{
        hotelSortCol = headerName;
        if (headerName.includes("評比") || headerName.includes("星級") || headerName.includes("價格")) {{
          hotelSortDir = "desc";
        }} else {{
          hotelSortDir = "asc";
        }}
      }}
      renderHotelSheet();
    }}

    function extractNumericValue(valStr, headerName) {{
      if (!valStr || valStr === "N/A" || valStr === "-") return -999999;
      const str = String(valStr).trim();
      
      if (headerName.includes("星級")) {{
        const m = str.match(/(\\d+)/);
        return m ? parseFloat(m[1]) : 0;
      }}
      
      if (headerName.includes("評比") || headerName.includes("Rating") || headerName.includes("Score")) {{
        const m = str.match(/(\\d+(?:\\.\\d+)?)/);
        return m ? parseFloat(m[1]) : 0;
      }}

      if (headerName.includes("價格") || headerName.includes("Price")) {{
        const clean = str.replace(/[^0-9]/g, '');
        return clean ? parseFloat(clean) : 0;
      }}

      return str;
    }}

    function renderHotelSheet() {{
      const sheet = HOTEL_EXCEL_DATA[currentHotelSheet];
      if (!sheet) return;

      const q = document.getElementById("hotelSearchInput").value.toLowerCase().trim();
      let filtered = sheet.rows.filter(row => {{
        if (!q) return true;
        return Object.values(row).some(v => String(v).toLowerCase().includes(q));
      }});

      if (hotelSortCol) {{
        filtered.sort((a, b) => {{
          const valA = extractNumericValue(a[hotelSortCol], hotelSortCol);
          const valB = extractNumericValue(b[hotelSortCol], hotelSortCol);

          if (typeof valA === "number" && typeof valB === "number") {{
            return hotelSortDir === "asc" ? valA - valB : valB - valA;
          }} else {{
            const sA = String(a[hotelSortCol] || "");
            const sB = String(b[hotelSortCol] || "");
            return hotelSortDir === "asc" ? sA.localeCompare(sB, "zh-Hant") : sB.localeCompare(sA, "zh-Hant");
          }}
        }});
      }}

      document.getElementById("hotelStatsBadge").textContent = `顯示 ${{filtered.length}} / ${{sheet.rows.length}} 筆飯店 (可點擊欄位排序)`;

      const thead = document.getElementById("hotelTableHead");
      const tbody = document.getElementById("hotelTableBody");
      
      thead.innerHTML = "<tr>" + sheet.headers.map(h => {{
        const isSorted = hotelSortCol === h;
        const icon = isSorted ? (hotelSortDir === "asc" ? "▲" : "▼") : "⇅";
        const cls = isSorted ? (hotelSortDir === "asc" ? "sorted-asc" : "sorted-desc") : "";
        return `<th class="${{cls}}" onclick="sortHotel('${{h}}')">${{h}} <span class="sort-icon">${{icon}}</span></th>`;
      }}).join("") + "</tr>";
      
      tbody.innerHTML = filtered.map(row => {{
        return "<tr>" + sheet.headers.map(h => {{
          const val = row[h] || "-";
          if (h.includes("加權平均") || h.includes("總平均")) {{
            return `<td><span class="weighted-badge">${{val}}</span></td>`;
          }}
          if (h.includes("價格")) {{
            return `<td><span class="price-text">${{val}}</span></td>`;
          }}
          if (h.includes("評比") && val !== "N/A" && val !== "-") {{
            return `<td><span class="score-badge">${{val}}</span></td>`;
          }}
          return `<td>${{val}}</td>`;
        }}).join("") + "</tr>";
      }}).join("");

      // Mobile Cards
      const cards = document.getElementById("hotelCardsContainer");
      cards.innerHTML = filtered.map(row => {{
        const name = row["飯店名稱 (Hotel Name)"] || row["飯店名稱"] || "飯店";
        const star = row["飯店星級 (Star)"] || row["飯店星級"] || "";
        let details = "";
        sheet.headers.forEach(h => {{
          if (h.includes("飯店名稱") || h.includes("星級")) return;
          const val = row[h] || "-";
          if (h.includes("加權平均") || h.includes("總平均")) {{
            details += `
              <div class="card-row" style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed #fecdd3;">
                <span class="card-label" style="color: var(--highlight-text); font-weight: bold;">${{h}}</span>
                <span class="card-val"><span class="weighted-badge">${{val}}</span></span>
              </div>`;
          }} else {{
            details += `
              <div class="card-row">
                <span class="card-label">${{h}}</span>
                <span class="card-val">${{val}}</span>
              </div>`;
          }}
        }});
        return `
          <div class="item-card">
            <div class="card-title-row">
              <div class="card-title">${{name}}</div>
              ${{star ? `<div class="card-star">${{star}}</div>` : ""}}
            </div>
            ${{details}}
          </div>`;
      }}).join("");
    }}

    // Food logic
    function filterFoodRibbon(val, btnEl) {{
      currentFoodRibbonFilter = val;
      const btns = document.querySelectorAll("#foodSubtabs .tab-btn");
      btns.forEach(b => b.className = "tab-btn");
      btnEl.className = "tab-btn active food-filter";
      renderFoodList();
    }}

    function sortFood(colName) {{
      if (foodSortCol === colName) {{
        foodSortDir = foodSortDir === "asc" ? "desc" : "asc";
      }} else {{
        foodSortCol = colName;
        foodSortDir = colName === "ribbon_count" ? "desc" : "asc";
      }}
      renderFoodList();
    }}

    function renderFoodList() {{
      const q = document.getElementById("foodSearchInput").value.toLowerCase().trim();
      let filtered = FOOD_DATA.filter(item => {{
        if (currentFoodRibbonFilter !== "ALL") {{
          if (String(item.ribbon_count) !== currentFoodRibbonFilter) return false;
        }}
        if (!q) return true;
        return (
          item.title_en.toLowerCase().includes(q) ||
          item.title_kr.toLowerCase().includes(q) ||
          item.cuisine_en.toLowerCase().includes(q) ||
          item.cuisine_kr.toLowerCase().includes(q) ||
          item.address_en.toLowerCase().includes(q) ||
          item.address_kr.toLowerCase().includes(q)
        );
      }});

      if (foodSortCol) {{
        filtered.sort((a, b) => {{
          const vA = a[foodSortCol];
          const vB = b[foodSortCol];
          if (typeof vA === "number" && typeof vB === "number") {{
            return foodSortDir === "asc" ? vA - vB : vB - vA;
          }} else {{
            const sA = String(vA || "");
            const sB = String(vB || "");
            return foodSortDir === "asc" ? sA.localeCompare(sB, "zh-Hant") : sB.localeCompare(sA, "zh-Hant");
          }}
        }});
      }}

      ["no", "title_en", "ribbon_count", "cuisine_en"].forEach(col => {{
        const iconEl = document.getElementById(`food_sort_${{col}}`);
        if (iconEl) {{
          if (foodSortCol === col) {{
            iconEl.textContent = foodSortDir === "asc" ? "▲" : "▼";
            iconEl.parentElement.className = `food-th ${{foodSortDir === "asc" ? "sorted-asc" : "sorted-desc"}}`;
          }} else {{
            iconEl.textContent = "⇅";
            iconEl.parentElement.className = "food-th";
          }}
        }}
      }});

      document.getElementById("foodStatsBadge").textContent = `顯示 ${{filtered.length}} / ${{FOOD_DATA.length}} 家餐廳 (可點擊欄位排序)`;

      // Food Table
      const tbody = document.getElementById("foodTableBody");
      tbody.innerHTML = filtered.map(item => {{
        let ribbonHtml = "";
        if (item.ribbon_count === 2) ribbonHtml = '<span class="ribbon-pill two">🎀🎀 2 個藍絲帶</span>';
        else if (item.ribbon_count === 1) ribbonHtml = '<span class="ribbon-pill">🎀 1 個藍絲帶</span>';
        else ribbonHtml = '<span style="color:#64748b; font-size:0.8rem;">⭐ 官方推薦 (0)</span>';

        return `
          <tr>
            <td style="text-align: center; font-weight: bold; color: #64748b;">${{item.no}}</td>
            <td>
              <div style="font-weight: 700; color: #0f172a;">${{item.title_en}}</div>
              <div style="color: #64748b; font-size: 0.85rem;">${{item.title_kr}}</div>
            </td>
            <td>${{ribbonHtml}}</td>
            <td>
              <div style="font-weight: 600;">${{item.cuisine_en}}</div>
              <div style="color: #64748b; font-size: 0.82rem;">${{item.cuisine_kr}}</div>
            </td>
            <td>
              <div style="font-size: 0.85rem;">${{item.address_en}}</div>
              <div style="margin-top: 2px;"><span class="addr-copy">${{item.address_kr}}</span></div>
            </td>
            <td style="text-align: center;">
              <a href="${{item.gmap_link}}" target="_blank" rel="noopener noreferrer" class="gmap-btn">
                📍 開啟地圖
              </a>
            </td>
            <td>
              <div style="font-size: 0.82rem; color: #334155;">${{item.time || '-'}}</div>
              ${{item.tag ? `<div class="tag-badge"># ${{item.tag}}</div>` : ''}}
            </td>
          </tr>
        `;
      }}).join("");

      // Food Cards (Mobile)
      const cards = document.getElementById("foodCardsContainer");
      cards.innerHTML = filtered.map(item => {{
        let ribbonHtml = "";
        if (item.ribbon_count === 2) ribbonHtml = '<span class="ribbon-pill two">🎀🎀 2 藍絲帶</span>';
        else if (item.ribbon_count === 1) ribbonHtml = '<span class="ribbon-pill">🎀 1 藍絲帶</span>';
        else ribbonHtml = '<span style="color:#64748b; font-size:0.8rem;">⭐ 官方推薦</span>';

        return `
          <div class="item-card" style="border-left: 4px solid ${{item.ribbon_count > 0 ? '#e11d48' : '#94a3b8'}};">
            <div class="card-title-row">
              <div>
                <div class="card-title">${{item.title_en}}</div>
                <div style="font-size: 0.85rem; color: #64748b;">${{item.title_kr}}</div>
              </div>
              <div>${{ribbonHtml}}</div>
            </div>
            <div class="card-row">
              <span class="card-label">飲食種類</span>
              <span class="card-val">${{item.cuisine_en}} (${{item.cuisine_kr}})</span>
            </div>
            <div class="card-row">
              <span class="card-label">韓文地址</span>
              <span class="card-val"><span class="addr-copy">${{item.address_kr}}</span></span>
            </div>
            <div class="card-row">
              <span class="card-label">地圖導航</span>
              <span class="card-val">
                <a href="${{item.gmap_link}}" target="_blank" rel="noopener noreferrer" class="gmap-btn">
                  📍 Google Map 導航
                </a>
              </span>
            </div>
            <div class="card-row">
              <span class="card-label">營業時間</span>
              <span class="card-val" style="font-size: 0.8rem; font-weight: normal;">${{item.time || '-'}}</span>
            </div>
            ${{item.tag ? `
            <div style="margin-top: 6px;">
              <span class="tag-badge"># ${{item.tag}}</span>
            </div>` : ''}}
          </div>
        `;
      }}).join("");
    }}

    // Init
    initHotelSubtabs();
    renderItinerary();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Portal index.html with 3 main tabs (Itinerary, Hotel, Food) built successfully!")
