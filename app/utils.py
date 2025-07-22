from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def extract_font_info(pdf_path):
    font_data = []

    for page_layout in extract_pages(pdf_path):
        page_num = page_layout.pageid
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    line_text = text_line.get_text().strip()
                    font_sizes = []
                    for char in text_line:
                        if isinstance(char, LTChar):
                            font_sizes.append(round(char.size, 1))
                    if line_text and font_sizes:
                        avg_font_size = sum(font_sizes) / len(font_sizes)
                        font_data.append({
                            "text": line_text,
                            "font_size": avg_font_size,
                            "page": page_num
                        })
    return font_data

def classify_headings(font_data):
    # Sort lines by font size (largest first)
    font_data_sorted = sorted(font_data, key=lambda x: x["font_size"], reverse=True)

    # Get top 3 unique font sizes
    unique_sizes = sorted({item["font_size"] for item in font_data_sorted}, reverse=True)
    top_fonts = unique_sizes[:3]  # Assume top 3 font sizes → H1, H2, H3

    headings = []
    for item in font_data_sorted:
        level = None
        if item["font_size"] == top_fonts[0]:
            level = "H1"
        elif len(top_fonts) > 1 and item["font_size"] == top_fonts[1]:
            level = "H2"
        elif len(top_fonts) > 2 and item["font_size"] == top_fonts[2]:
            level = "H3"

        if level:
            headings.append({
                "level": level,
                "text": item["text"],
                "page": item["page"]
            })

    return headings
def remove_duplicates(headings):
    seen = set()
    unique = []
    for h in headings:
        key = (h["level"], h["text"].strip().lower())
        if key not in seen:
            seen.add(key)
            unique.append(h)
    return unique
