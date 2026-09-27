import json

with open('excel_data.json', 'r', encoding='utf-8') as f:
    hotel_data_str = f.read()

with open('visitbusan_100_places.json', 'r', encoding='utf-8') as f:
    en_places = json.load(f)

with open('visitbusan_100_places_kr.json', 'r', encoding='utf-8') as f:
    kr_places = json.load(f)

# Combine food data
food_data = []
for i in range(len(en_places)):
    e = en_places[i]
    k = kr_places[i]
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
        'link': e['detail_link']
    })

food_json_str = json.dumps(food_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2026年12月 韓國釜山旅遊指南：住 (Hotel) ＆ 食 (Food 100選)</title>
  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-light: #2563eb;
      --food-primary: #b91c1c;
      --food-light: #dc2626;
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
      line-height: 1.5;
      padding-bottom: 60px;
    }}

    /* Global Header */
    header {{
      background: linear-gradient(135deg, #091325 0%, #1e3a8a 60%, #881337 100%);
      color: white;
      padding: 30px 20px 24px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    }}
    header h1 {{ font-size: 1.85rem; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.5px; }}
    header p {{ font-size: 0.95rem; color: #cbd5e1; max-width: 900px; margin: 0 auto; }}

    /* Main Category Toggle: 住 (Hotel) vs 食 (Food) */
    .main-nav-wrapper {{
      max-width: 800px;
      margin: 18px auto 0;
      display: flex;
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(8px);
      padding: 5px;
      border-radius: 9999px;
      border: 1px solid rgba(255,255,255,0.25);
    }}
    .main-nav-btn {{
      flex: 1;
      padding: 10px 20px;
      border: none;
      background: transparent;
      color: #e2e8f0;
      font-size: 1.05rem;
      font-weight: 700;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .main-nav-btn.active.hotel {{
      background: #1e3a8a;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }}
    .main-nav-btn.active.food {{
      background: #b91c1c;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }}

    .container {{
      max-width: 1400px;
      margin: 20px auto;
      padding: 0 16px;
    }}

    /* Sub-tabs Navigation for Hotel */
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

    /* Desktop Table */
    .table-container {{
      background: var(--card-bg);
      border-radius: 10px;
      border: 1px solid var(--border);
      overflow-x: auto;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      display: block;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }}
    th {{
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
      position: sticky;
      top: 0;
      z-index: 10;
    }}
    th.food-th {{
      background: #fef2f2;
      color: #991b1b;
    }}
    td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
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
    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text);
    }}
    .card-star {{
      background: #fef3c7;
      color: #b45309;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      white-space: nowrap;
    }}
    .card-row {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 6px;
      font-size: 0.85rem;
    }}
    .card-label {{ color: var(--text-muted); font-weight: 500; min-width: 90px; }}
    .card-val {{ font-weight: 600; text-align: right; word-break: break-word; }}

    /* Badges */
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
    .ribbon-pill.two {{
      background: #fdf2f8;
      color: #be185d;
      border-color: #fbcfe8;
    }}
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

    @media (max-width: 900px) {{
      .table-container {{ display: none; }}
      .cards-container {{ display: flex; }}
      header h1 {{ font-size: 1.4rem; }}
      .control-bar {{ padding: 10px; }}
      .tab-btn {{ padding: 8px 12px; font-size: 0.82rem; }}
    }}
  </style>
</head>
<body>

  <header>
    <h1>🇰🇷 2026年12月 韓國釜山旅遊全方位指南</h1>
    <p>日期：2026/12/3 ~ 12/8 (5晚雙人自由行) | 精選住宿大數據評比 ＆ Visit Busan 100選名店指南</p>
    
    <!-- Main Tab Selector -->
    <div class="main-nav-wrapper">
      <button class="main-nav-btn active hotel" id="mainTabHotel" onclick="switchMainSection('hotel')">
        🏨 住宿評比 (Hotel - Agent)
      </button>
      <button class="main-nav-btn food" id="mainTabFood" onclick="switchMainSection('food')">
        🍽️ 釜山100選美食 (Food - 100 Great Places)
      </button>
    </div>
  </header>

  <div class="container">
    
    <!-- SECTION 1: HOTEL -->
    <div id="hotelSection">
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
              <th class="food-th" style="width: 50px; text-align: center;">No.</th>
              <th class="food-th">店名 (英文 / 韓文)</th>
              <th class="food-th">Blue Ribbon 評級</th>
              <th class="food-th">料理種類</th>
              <th class="food-th">地址 (可複製導航)</th>
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

    let currentMainSection = "hotel";
    let currentHotelSheet = "綜合總結比價 (Summary)";
    let currentFoodRibbonFilter = "ALL";

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
      const hotelBtn = document.getElementById("mainTabHotel");
      const foodBtn = document.getElementById("mainTabFood");
      const hotelSec = document.getElementById("hotelSection");
      const foodSec = document.getElementById("foodSection");

      if (sec === "hotel") {{
        hotelBtn.className = "main-nav-btn active hotel";
        foodBtn.className = "main-nav-btn food";
        hotelSec.style.display = "block";
        foodSec.style.display = "none";
        renderHotelSheet();
      }} else {{
        hotelBtn.className = "main-nav-btn hotel";
        foodBtn.className = "main-nav-btn active food";
        hotelSec.style.display = "none";
        foodSec.style.display = "block";
        renderFoodList();
      }}
    }}

    // Hotel logic
    function initHotelSubtabs() {{
      const c = document.getElementById("hotelSubtabs");
      c.innerHTML = "";
      hotelTabs.forEach(t => {{
        const btn = document.createElement("button");
        btn.className = `tab-btn ${{t.name === currentHotelSheet ? "active" : ""}}`;
        btn.innerHTML = `${{t.icon}} ${{t.label}}`;
        btn.onclick = () => {{
          currentHotelSheet = t.name;
          initHotelSubtabs();
          document.getElementById("hotelSearchInput").value = "";
          renderHotelSheet();
        }};
        c.appendChild(btn);
      }});
    }}

    function renderHotelSheet() {{
      const sheet = HOTEL_EXCEL_DATA[currentHotelSheet];
      if (!sheet) return;

      const q = document.getElementById("hotelSearchInput").value.toLowerCase().trim();
      const filtered = sheet.rows.filter(row => {{
        if (!q) return true;
        return Object.values(row).some(v => String(v).toLowerCase().includes(q));
      }});

      document.getElementById("hotelStatsBadge").textContent = `顯示 ${{filtered.length}} / ${{sheet.rows.length}} 筆飯店`;

      const thead = document.getElementById("hotelTableHead");
      const tbody = document.getElementById("hotelTableBody");
      thead.innerHTML = "<tr>" + sheet.headers.map(h => `<th>${{h}}</th>`).join("") + "</tr>";
      
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

      // Mobile
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

    function renderFoodList() {{
      const q = document.getElementById("foodSearchInput").value.toLowerCase().trim();
      const filtered = FOOD_DATA.filter(item => {{
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

      document.getElementById("foodStatsBadge").textContent = `顯示 ${{filtered.length}} / ${{FOOD_DATA.length}} 家餐廳`;

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
    renderHotelSheet();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Portal index.html with Hotel & Food tabs built successfully!")
