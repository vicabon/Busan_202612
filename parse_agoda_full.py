import re

with open('Agoda_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('---PAGE---')

all_hotels = []

for p_idx in range(len(pages)-1):
    p = pages[p_idx]
    
    # 1) Find 1/10 cards for hotel name and location score
    cards_110 = p.split('1/10')[1:]
    
    # 2) Find review/score/price blocks in the page
    # In Agoda raw text, the list items appear with:
    # score + label: r'(\d+\.\d+)\s+(Exceptional|Excellent|Very [Gg]ood)'
    # reviews: r'([\d,]+)\s+reviews'
    # price: r'NT\$\s*([\d,]+)' or 'Sold out on your'
    
    # Let's extract all (score, rev_count) pairs from page
    # Notice that sometimes in sponsored/deals section there are extra, but in main cards:
    rev_blocks = []
    lines = [l.strip() for l in p.split('\n') if l.strip()]
    for i, l in enumerate(lines):
        m_rev = re.search(r'^([\d,]+)\s+reviews$', l)
        if m_rev:
            rev_cnt = m_rev.group(1)
            # score is usually in previous line
            score = 'N/A'
            if i > 0:
                m_sc = re.search(r'(\d+\.\d+)\s+(?:Exceptional|Excellent|Very [Gg]ood)', lines[i-1])
                if m_sc:
                    score = m_sc.group(1)
            # price is usually in next few lines
            price = 'N/A'
            for j in range(i+1, min(len(lines), i+8)):
                if 'Per night' in lines[j]:
                    # look at lines[j-1] or lines[j]
                    m_p = re.search(r'NT\$\s*([\d,]+)', lines[j-1] + ' ' + lines[j])
                    if m_p:
                        price = f"NT$ {m_p.group(1)}"
                        break
                elif 'Sold out' in lines[j]:
                    price = 'Sold out'
                    break
            rev_blocks.append({'score': score, 'rev_count': rev_cnt, 'price': price})
            
    print(f"Page {p_idx}: cards_110={len(cards_110)}, rev_blocks={len(rev_blocks)}")

