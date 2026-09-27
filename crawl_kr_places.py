import requests
from bs4 import BeautifulSoup
import time
import json

base_url = "https://www.visitbusan.net/index.do?menuCd=DOM_000000201002002000&listCntPerPage2=12&page_no={}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

kr_places = []

for page in range(1, 11):
    url = base_url.format(page)
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, 'html.parser')
        blue_ribbon = soup.find('div', class_='blueRibbon')
        if not blue_ribbon:
            break
        items = blue_ribbon.find_all('li', class_='contents')
        if not items:
            break
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
            
            tag_ul = a.find('li', class_='tag')
            tag_text = tag_ul.get_text(strip=True) if tag_ul else ''
            
            kr_places.append({
                'title_kr': title,
                'cuisine_kr': exp,
                'address_kr': addr,
                'operating_time_kr': time_info,
                'ribbon_count': ribbon_count,
                'tag_kr': tag_text
            })
    except Exception as e:
        print(f"Exception on KR page {page}: {e}")
        break
    time.sleep(0.3)

print(f"Total KR places collected: {len(kr_places)}")
with open('visitbusan_100_places_kr.json', 'w', encoding='utf-8') as f:
    json.dump(kr_places, f, ensure_ascii=False, indent=2)
print("Saved to visitbusan_100_places_kr.json")
