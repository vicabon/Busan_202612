import pdfplumber, re

# In Trip.com, every hotel listing starts with an image/container,
# has a Hotel Name, stars, review count, rating score (x.x/10),
# location string (after 'Show on Map'), per night price, total price.

with pdfplumber.open('Hotels/Trip - Where to stay in Busan _ Trip.com.pdf') as pdf:
    total_parsed = 0
    all_hotels = []
    for page_idx in range(len(pdf.pages)):
        p = pdf.pages[page_idx]
        words = sorted(p.extract_words(), key=lambda w: (w['top'], w['x0']))
        # find all score words e.g. '9.2/10'
        score_words = [w for w in words if re.match(r'^\d+\.\d+/10$', w['text'])]
        
        # Each score word represents one hotel card on this page!
        for sw in score_words:
            # card y range: roughly sw['top'] - 40 to sw['top'] + 80
            card_words = [w for w in words if abs(w['top'] - sw['top']) < 65]
            # print snippet
            c_text = " ".join([w['text'] for w in sorted(card_words, key=lambda w: (round(w['top']/4)*4, w['x0']))])
            all_hotels.append({'page': page_idx, 'top': sw['top'], 'score': sw['text'], 'snippet': c_text[:120]})
            total_parsed += 1

    print(f"Total cards mapped via score words: {total_parsed}")
    for h in all_hotels[:10]:
        print(h)
