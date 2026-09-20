import pdfplumber, re

with pdfplumber.open('Hotels/Trip - Where to stay in Busan _ Trip.com.pdf') as pdf:
    for page_idx in range(2):
        p = pdf.pages[page_idx]
        words = sorted(p.extract_words(), key=lambda w: (w['top'], w['x0']))
        # Find score words
        score_words = [w for w in words if '/10' in w['text']]
        # Find price words 'Total' 'price:'
        # Find hotel names: usually font size larger or specific coordinates
        print(f"=== Page {page_idx} ===")
        for sw in score_words:
            # find words around this y
            nearby = [w for w in words if abs(w['top'] - sw['top']) < 15]
            print(f"y={sw['top']:.1f}: " + " ".join([w['text'] for w in nearby]))

