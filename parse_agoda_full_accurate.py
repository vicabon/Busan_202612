import re

with open('Agoda_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('---PAGE---')

all_agoda = []

for p_idx in range(len(pages)-1):
    p = pages[p_idx]
    cards_110 = p.split('1/10')[1:]
    
    # review blocks
    lines = [l.strip() for l in p.split('\n') if l.strip()]
    rev_blocks = []
    for i, l in enumerate(lines):
        m_rev = re.search(r'^([\d,]+)\s+reviews$', l)
        if m_rev:
            rev_cnt = m_rev.group(1)
            score = 'N/A'
            if i > 0:
                m_sc = re.search(r'(\d+\.\d+)\s+(?:Exceptional|Excellent|Very [Gg]ood)', lines[i-1])
                if m_sc: score = m_sc.group(1)
            price = 'N/A'
            for j in range(i+1, min(len(lines), i+8)):
                if 'Per night' in lines[j]:
                    m_p = re.search(r'NT\$\s*([\d,]+)', lines[j-1] + ' ' + lines[j])
                    if m_p:
                        price = f"NT$ {m_p.group(1)} / 晚"
                        break
                elif 'Sold out' in lines[j]:
                    price = '已售完 (Sold out)'
                    break
            rev_blocks.append({'score': score, 'rev_count': rev_cnt, 'price': price})
            
    for c_idx, c in enumerate(cards_110):
        c_lines = [l.strip() for l in c.split('\n') if l.strip()]
        loc_score = 'N/A'
        for l in c_lines:
            m = re.search(r'(\d+\.\d+)\s+Location score', l)
            if m:
                loc_score = m.group(1)
                break
                
        stars = 'N/A'
        for l in c_lines:
            if '3-star' in l: stars = '3星級'
            elif '4-star' in l: stars = '4星級'
            elif '5-star' in l: stars = '5星級'
            
        cand_names = [l for l in c_lines if not ('Location score' in l or 'applied' in l or re.match(r'^\d[\d,]*$', l) or 'to center' in l or 'City center' in l or 'Best rated' in l or 'Award' in l or 'Newly renovated' in l or 'SEARCH' in l or 'Agoda' in l or 'http' in l or 'adults' in l or 'room' in l or 'Dec 2026' in l or 'Thursday' in l or 'Tuesday' in l)]
        
        hotel_name = cand_names[0] if cand_names else 'Unknown'
        if len(cand_names) > 1:
            if len(cand_names[0]) < 12 and not any(k in cand_names[0] for k in ['Hotel', 'Suites', 'Resort', 'Condo']):
                hotel_name = f"{cand_names[0]} {cand_names[1]}"
            elif any(k in cand_names[1] for k in ['HOTELS', 'Beach', 'Resort', 'Station', 'Residence', 'Stay', 'Seomyeon', 'Haeundae']):
                hotel_name = f"{cand_names[0]} {cand_names[1]}"
                
        rb = rev_blocks[c_idx] if c_idx < len(rev_blocks) else {'score': 'N/A', 'rev_count': 'N/A', 'price': 'N/A'}
        
        all_agoda.append({
            'name': hotel_name,
            'stars': stars,
            'price': rb['price'],
            'guest_score': rb['score'],
            'rev_count': rb['rev_count'],
            'loc_score': loc_score
        })

print(f"Total Agoda parsed: {len(all_agoda)} hotels")
for h in all_agoda[:10]:
    print(h)
