import os
import json
from utils import extract_font_info, classify_headings,remove_duplicates

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def get_title(font_data):
    # Assume the largest text on the first page is the title
    page1_texts = [d for d in font_data if d["page"] == 1]
    if page1_texts:
        return sorted(page1_texts, key=lambda x: x["font_size"], reverse=True)[0]["text"]
    return "Untitled"

def process_pdf(file_path, output_path):
    font_data = extract_font_info(file_path)
    title = get_title(font_data)
    headings = classify_headings(font_data)
    headings = remove_duplicates(headings)
    headings = sorted(headings, key=lambda x: x["page"])

    result = {
        "title": title,
        "outline": headings
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_pdf = os.path.join(INPUT_DIR, filename)
            output_json = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            process_pdf(input_pdf, output_json)

if __name__ == "__main__":
    main()
