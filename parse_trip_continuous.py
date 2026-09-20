import re

with open('Trip_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove page header / footer lines across pages
lines = []
for l in text.split('\n'):
    l_str = l.strip()
    # filter out page breaks and browser print headers/footers
    if '---PAGE---' in l_str or 'Busan Hotels - Where to stay' in l_str or 'https://www.trip.com/hotels/list?' in l_str:
        continue
    # filter out the sidebar/filter noise that repeats at page bottom
    if any(k in l_str for k in ['Popular filters for Busan', 'Clear Filters', 'Search󱖍5 nights', 'Straight-line distance', 'Diamond rating', 'Based on guest reviews', 'Customer support Find bookings']):
        continue
    lines.append(l_str)

full_cleaned_text = '\n'.join(lines)
cards = full_cleaned_text.split('Check Availability')

all_trip = []
all_scores = re.findall(r'(\d+\.\d+)/10', full_cleaned_text)

for c_idx, c in enumerate(cards[:-1]):
    c_lines = [l.strip() for l in c.split('\n') if l.strip()]
    
    per_night = 'N/A'
    total_price = 'N/A'
    for l in c_lines:
        if l.startswith('Total price:'):
            total_price = l.replace('Total price:', '').strip()
        elif l.startswith('TWD') and 'Total' not in l:
            per_night = l.strip()
            
    price_str = f"{per_night} / 晚 (總額 {total_price})" if total_price != 'N/A' else per_night
    
    rev_count = 'N/A'
    for l in c_lines:
        m_rev = re.search(r'([\d,]+)\s+reviews', l)
        if m_rev and rev_count == 'N/A':
            rev_count = m_rev.group(1)
            
    hotel_name = 'Unknown'
    stars = 'N/A'
    
    # Check lines for reviews and take previous line as name
    for i, l in enumerate(c_lines):
        if 'reviews' in l and i > 0:
            name_cand = c_lines[i-1]
            s_count = name_cand.count('\U000f1428') + name_cand.count('\U000f1445')
            if s_count > 0:
                stars = f"{s_count}星級"
            clean_n = re.sub(r'[\U00010000-\U0010ffff]', '', name_cand)
            clean_n = re.sub(r'Opened in \d+', '', clean_n)
            clean_n = re.sub(r'Diamond rating.*', '', clean_n).strip()
            if clean_n and len(clean_n) > 2:
                hotel_name = clean_n
            break
            
    if hotel_name == 'Unknown':
        for l in c_lines:
            if '\U000f1428' in l or '\U000f1445' in l:
                s_count = l.count('\U000f1428') + l.count('\U000f1445')
                if s_count > 0:
                    stars = f"{s_count}星級"
                clean_n = re.sub(r'[\U00010000-\U0010ffff]', '', l)
                clean_n = re.sub(r'Opened in \d+', '', clean_n)
                clean_n = re.sub(r'Diamond rating.*', '', clean_n).strip()
                if clean_n and len(clean_n) > 2:
                    hotel_name = clean_n
                    break
                    
    loc_desc = 'N/A'
    for l in c_lines:
        if 'Show on Map' in l:
            loc_desc = l.replace('Show on Map', '').replace('\U000f1421', '').strip()
            break
            
    guest_score = all_scores[c_idx] if c_idx < len(all_scores) else 'N/A'
    
    all_trip.append({
        'name': hotel_name,
        'stars': stars,
        'price': price_str,
        'guest_score': guest_score,
        'rev_count': rev_count,
        'loc_score': loc_desc
    })

print(f"Parsed continuous Trip: {len(all_trip)} cards")
unknowns = [h for h in all_trip if h['name'] == 'Unknown']
print(f"Unknowns count: {len(unknowns)}")
for h in all_trip[:10]:
    print(h)
