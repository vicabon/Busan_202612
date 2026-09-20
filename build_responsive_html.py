import json

with open('excel_data.json', 'r', encoding='utf-8') as f:
    data = f.read()

html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2026年12月韓國釜山住宿大數據評比與比價網 (GitHub Pages)</title>
  <style>
    :root {
      --primary: #1e3a8a;
      --primary-light: #3b82f6;
      --accent: #e11d48;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --text: #0f172a;
      --text-muted: #64748b;
      --highlight-bg: #fff1f2;
      --highlight-text: #be123c;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft JhengHei", sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 50px;
    }

    /* Header */
    header {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: white;
      padding: 30px 20px;
      text-align: center;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    header h1 { font-size: 1.8rem; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.5px; }
    header p { font-size: 0.95rem; color: #cbd5e1; max-width: 800px; margin: 0 auto; }
    .badge-container { display: flex; justify-content: center; gap: 8px; margin-top: 14px; flex-wrap: wrap; }
    .badge {
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(4px);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.8rem;
      border: 1px solid rgba(255,255,255,0.2);
    }

    /* Container */
    .container {
      max-width: 1400px;
      margin: 20px auto;
      padding: 0 16px;
    }

    /* Tabs Navigation */
    .tabs-wrapper {
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--bg);
      padding: 10px 0;
    }
    .tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      -webkit-overflow-scrolling: touch;
    }
    .tabs::-webkit-scrollbar { height: 4px; }
    .tabs::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    
    .tab-btn {
      padding: 10px 18px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tab-btn:hover { background: #f1f5f9; color: var(--text); }
    .tab-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
      box-shadow: 0 4px 10px rgba(30, 58, 138, 0.25);
    }

    /* Search & Filter Bar */
    .control-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin: 16px 0;
      background: var(--card-bg);
      padding: 14px;
      border-radius: 10px;
      border: 1px solid var(--border);
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      align-items: center;
    }
    .search-input {
      flex: 1;
      min-width: 240px;
      padding: 10px 14px;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.95rem;
      outline: none;
      transition: border 0.2s;
    }
    .search-input:focus { border-color: var(--primary-light); }
    .stats-badge {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-left: auto;
    }

    /* Desktop Table View */
    .table-container {
      background: var(--card-bg);
      border-radius: 10px;
      border: 1px solid var(--border);
      overflow-x: auto;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      display: block;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }
    th {
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }
    tr:hover td { background-color: #f8fafc; }
    tr:nth-child(even) td { background-color: #fafafa; }

    /* Mobile Card View (shown on smaller screens) */
    .cards-container {
      display: none;
      flex-direction: column;
      gap: 14px;
    }
    .hotel-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      transition: transform 0.15s, box-shadow 0.15s;
    }
    .hotel-card:active { transform: scale(0.99); }
    .card-title-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
      margin-bottom: 10px;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 10px;
    }
    .card-hotel-name {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text);
    }
    .card-hotel-star {
      background: #fef3c7;
      color: #b45309;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      white-space: nowrap;
    }
    .card-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 6px;
      font-size: 0.85rem;
    }
    .card-label { color: var(--text-muted); font-weight: 500; }
    .card-val { font-weight: 600; text-align: right; }

    /* Weighted Average Pill */
    .weighted-badge {
      display: inline-block;
      background: var(--highlight-bg);
      color: var(--highlight-text);
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      border: 1px solid #fecdd3;
    }
    .score-badge {
      display: inline-block;
      background: #f0fdf4;
      color: #166534;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.85rem;
    }
    .price-text {
      color: #0369a1;
      font-weight: 700;
    }

    /* Responsive Mode Toggle */
    @media (max-width: 900px) {
      .table-container { display: none; }
      .cards-container { display: flex; }
      header h1 { font-size: 1.4rem; }
      .control-bar { padding: 10px; }
      .tab-btn { padding: 8px 14px; font-size: 0.85rem; }
    }
  </style>
</head>
<body>

  <header>
    <h1>2026年12月 韓國釜山住宿大數據評比與比價總表</h1>
    <p>日期：2026/12/3 ~ 12/8（5晚雙人自由行） | 每晚預算 0~5000 NTD | 3星級以上 | 客戶評比 8+ 優秀</p>
    <div class="badge-container">
      <span class="badge">Agoda.com</span>
      <span class="badge">Booking.com</span>
      <span class="badge">Trip.com</span>
      <span class="badge">Tripadvisor</span>
      <span class="badge">Google Map</span>
      <span class="badge">跨網加權總平均</span>
    </div>
  </header>

  <div class="container">
    <!-- Tabs -->
    <div class="tabs-wrapper">
      <div class="tabs" id="tabContainer"></div>
    </div>

    <!-- Search / Filter Bar -->
    <div class="control-bar">
      <input type="text" id="searchInput" class="search-input" placeholder="🔍 搜尋飯店名稱、星級、地點或關鍵字..." oninput="renderCurrentSheet()">
      <div class="stats-badge" id="statsBadge">顯示 0 / 0 筆</div>
    </div>

    <!-- Desktop Table View -->
    <div class="table-container">
      <table id="dataTable">
        <thead id="tableHead"></thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>

    <!-- Mobile Card View -->
    <div class="cards-container" id="cardsContainer"></div>
  </div>

  <script>
    const EXCEL_DATA = """ + data + """;
    let currentSheetName = "綜合總結比價 (Summary)";

    const sheetTabs = [
      { name: "綜合總結比價 (Summary)", label: "📊 綜合比價與加權總評", icon: "⭐" },
      { name: "Agoda.com", label: "Agoda.com", icon: "🔴" },
      { name: "Booking.com", label: "Booking.com", icon: "🔵" },
      { name: "Trip.com", label: "Trip.com", icon: "🌐" },
      { name: "Tripadvisor.com", label: "Tripadvisor", icon: "🟢" },
      { name: "Google Map", label: "Google Map", icon: "🟠" }
    ];

    function initTabs() {
      const tabContainer = document.getElementById("tabContainer");
      tabContainer.innerHTML = "";
      sheetTabs.forEach(t => {
        const btn = document.createElement("button");
        btn.className = `tab-btn ${t.name === currentSheetName ? "active" : ""}`;
        btn.innerHTML = `${t.icon} ${t.label}`;
        btn.onclick = () => switchTab(t.name);
        tabContainer.appendChild(btn);
      });
    }

    function switchTab(name) {
      currentSheetName = name;
      initTabs();
      document.getElementById("searchInput").value = "";
      renderCurrentSheet();
    }

    function renderCurrentSheet() {
      const sheet = EXCEL_DATA[currentSheetName];
      if (!sheet) return;

      const query = document.getElementById("searchInput").value.toLowerCase().trim();
      const filteredRows = sheet.rows.filter(row => {
        if (!query) return true;
        return Object.values(row).some(v => String(v).toLowerCase().includes(query));
      });

      document.getElementById("statsBadge").textContent = `顯示 ${filteredRows.length} / ${sheet.rows.length} 筆飯店`;

      // 1. Render Desktop Table
      const thead = document.getElementById("tableHead");
      const tbody = document.getElementById("tableBody");
      
      thead.innerHTML = "<tr>" + sheet.headers.map(h => `<th>${h}</th>`).join("") + "</tr>";
      tbody.innerHTML = filteredRows.map(row => {
        return "<tr>" + sheet.headers.map((h, i) => {
          const val = row[h] || "-";
          if (h.includes("加權平均") || h.includes("總平均")) {
            return `<td><span class="weighted-badge">${val}</span></td>`;
          }
          if (h.includes("價格")) {
            return `<td><span class="price-text">${val}</span></td>`;
          }
          if (h.includes("評比") && val !== "N/A" && val !== "-") {
            return `<td><span class="score-badge">${val}</span></td>`;
          }
          return `<td>${val}</td>`;
        }).join("") + "</tr>";
      }).join("");

      // 2. Render Mobile Cards
      const cardsContainer = document.getElementById("cardsContainer");
      cardsContainer.innerHTML = filteredRows.map(row => {
        const hotelName = row["飯店名稱 (Hotel Name)"] || row["飯店名稱"] || "飯店";
        const star = row["飯店星級 (Star)"] || row["飯店星級"] || "";
        
        let detailsHtml = "";
        sheet.headers.forEach(h => {
          if (h.includes("飯店名稱") || h.includes("星級")) return;
          const val = row[h] || "-";
          if (h.includes("加權平均") || h.includes("總平均")) {
            detailsHtml += `
              <div class="card-row" style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed #fecdd3;">
                <span class="card-label" style="color: var(--highlight-text); font-weight: bold;">${h}</span>
                <span class="card-val"><span class="weighted-badge">${val}</span></span>
              </div>`;
          } else {
            detailsHtml += `
              <div class="card-row">
                <span class="card-label">${h}</span>
                <span class="card-val">${val}</span>
              </div>`;
          }
        });

        return `
          <div class="hotel-card">
            <div class="card-title-row">
              <div class="card-hotel-name">${hotelName}</div>
              ${star ? `<div class="card-hotel-star">${star}</div>` : ""}
            </div>
            ${detailsHtml}
          </div>
        `;
      }).join("");
    }

    // Init
    initTabs();
    renderCurrentSheet();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("index.html created successfully!")
