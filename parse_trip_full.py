import re

with open('Trip_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('---PAGE---')

all_trip = []

for p_idx, p in enumerate(pages):
    # cards end with 'Check Availability'
    cards = p.split('Check Availability')
    # the last item in cards is footer/after last card, or if page boundary splits
    for c_idx, c in enumerate(cards[:-1]):
        lines = [l.strip() for l in c.split('\n') if l.strip()]
        
        # Find price
        per_night = 'N/A'
        total_price = 'N/A'
        for l in lines:
            if l.startswith('Total price:'):
                total_price = l.replace('Total price:', '').strip()
            elif l.startswith('TWD') and 'Total' not in l:
                per_night = l.strip()
                
        # Find reviews and guest rating
        rev_count = 'N/A'
        guest_score = 'N/A'
        loc_score = 'N/A'
        
        # In Trip card:
        # e.g. Great 1,240 reviews "Great swimming pool"
        # and on the right side: 9.2/10
        for l in lines:
            m_rev = re.search(r'([\d,]+)\s+reviews', l)
            if m_rev and rev_count == 'N/A':
                rev_count = m_rev.group(1)
            m_sc = re.search(r'(\d+\.\d+)/10', l)
            if m_sc and guest_score == 'N/A':
                guest_score = m_sc.group(1)
                
        # Find star rating and hotel name
        # Looking for lines with \U000f1428 or \U000f1445 or lines right before reviews
        hotel_name = 'Unknown'
        stars = 'N/A'
        for i, l in enumerate(lines):
            if 'reviews' in l and i > 0:
                name_cand = lines[i-1]
                # count stars
                s_count = name_cand.count('\U000f1428') + name_cand.count('\U000f1445')
                if s_count > 0:
                    stars = f"{s_count}星級"
                # clean name
                clean_n = re.sub(r'[\U00010000-\U0010ffff]', '', name_cand)
                clean_n = re.sub(r'Opened in \d+', '', clean_n)
                clean_n = re.sub(r'Diamond rating.*', '', clean_n).strip()
                if clean_n:
                    hotel_name = clean_n
                break
                
        # Find location info / rating
        # Location info is after 'Show on Map'
        for l in lines:
            if 'Show on Map' in l:
                loc_score = l.replace('Show on Map', '').replace('\U000f1421', '').strip()
                break
                
        all_trip.append({
            'page': p_idx,
            'name': hotel_name,
            'stars': stars,
            'per_night': per_night,
            'total_price': total_price,
            'guest_score': guest_score,
            'rev_count': rev_count,
            'loc_score': loc_score
        })

print(f"Total Trip hotels parsed: {len(all_trip)}")
for t in all_trip[:8]:
    print(t)
