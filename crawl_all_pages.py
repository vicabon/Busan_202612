import requests
from bs4 import BeautifulSoup
import time
import json

base_url = "https://www.visitbusan.net/index.do?menuCd=DOM_000000301002002000&listCntPerPage2=12&page_no={}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

all_places = []

for page in range(1, 15):
    url = base_url.format(page)
    print(f"Fetching page {page}...")
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code != 200:
            print(f"Error status {resp.status_code} on page {page}")
            break
        soup = BeautifulSoup(resp.text, 'html.parser')
        blue_ribbon = soup.find('div', class_='blueRibbon')
        if not blue_ribbon:
            print(f"No blueRibbon div on page {page}")
            break
        items = blue_ribbon.find_all('li', class_='contents')
        if not items:
            print(f"No items on page {page}")
            break
        print(f"Page {page}: found {len(items)} items")
        for it in items:
            a = it.find('a')
            if not a: continue
            title = a.find('div', class_='title').get_text(strip=True) if a.find('div', class_='title') else ''
            exp = a.find('p', class_='exp').get_text(strip=True) if a.find('p', class_='exp') else ''
            addr = a.find('li', class_='adress').get_text(strip=True) if a.find('li', class_='adress') else ''
            time_info = a.find('li', class_='time').get_text(strip=True) if a.find('li', class_='time') else ''
            
            # ribbons
            ribbon_ul = a.find('ul', class_='ribbon')
            ribbon_imgs = ribbon_ul.find_all('img') if ribbon_ul else []
            ribbon_count = len(ribbon_imgs)
            
            # tags
            tag_ul = a.find('li', class_='tag')
            tag_text = tag_ul.get_text(strip=True) if tag_ul else ''
            
            detail_link = a.get('href', '')
            if detail_link and not detail_link.startswith('http'):
                detail_link = "https://www.visitbusan.net" + detail_link
                
            all_places.append({
                'title': title,
                'cuisine': exp,
                'address': addr,
                'operating_time': time_info,
                'ribbon_count': ribbon_count,
                'tag': tag_text,
                'detail_link': detail_link
            })
    except Exception as e:
        print(f"Exception on page {page}: {e}")
        break
    time.sleep(0.5)

print(f"Total places collected: {len(all_places)}")
with open('visitbusan_100_places.json', 'w', encoding='utf-8') as f:
    json.dump(all_places, f, ensure_ascii=False, indent=2)
print("Saved to visitbusan_100_places.json")
