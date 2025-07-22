# 📄 PDF Outline Extractor – Adobe Hackathon 2025 (Round 1A)

## 🚀 Challenge: "Connecting the Dots Through Docs"

This project is built for **Round 1A** of the Adobe India Hackathon 2025.  
The goal is to extract a **structured outline** from a PDF document, including:
- The **Title**
- Headings with levels: `H1`, `H2`, `H3`
- Corresponding **page numbers**

The output is generated in a clean **JSON format**, ready to power intelligent document experiences.

---

## 🧠 Approach

1. **PDF Parsing**: The solution uses [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six) to extract text and font information from each page.
2. **Font-Based Grouping**:
   - Each line is analyzed for its **average font size**
   - The largest font size is assumed to be the **title**
   - Next 2 largest sizes are mapped to `H1`, `H2`, and `H3`
3. **Structured JSON Output**: The final result includes a JSON with title and a list of hierarchical headings with their levels and page numbers.

---

## 📦 Input & Output Format

### 🖇️ Input:
Place one or more `.pdf` files (≤ 50 pages each) in the `input/` folder.

### 📤 Output:
The system generates `.json` files with the same filename in the `output/` folder.

Example:
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
