from pathlib import Path
import fitz  
import json

def extract_headings_from_pdf(pdf_path):
    print(f"Inside extract_headings_from_pdf for {pdf_path.name}")
    doc = fitz.open(pdf_path)
    title = ""
    headings = []
    font_sizes = {}

    for page_num, page in enumerate(doc, start=0):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = round(span["size"], 1)
                    if not text:
                        continue

                    font_sizes[size] = font_sizes.get(size, 0) + 1

                    headings.append({
                        "text": text,
                        "size": size,
                        "page": page_num
                    })

    unique_sizes = sorted(font_sizes, reverse=True)
    size_to_level = {}
    if unique_sizes:
        size_to_level[unique_sizes[0]] = "H1"
        if len(unique_sizes) > 1:
            size_to_level[unique_sizes[1]] = "H2"
        if len(unique_sizes) > 2:
            size_to_level[unique_sizes[2]] = "H3"

    title_candidates = [h for h in headings if h["page"] == 1 and h["size"] == unique_sizes[0]]
    if title_candidates:
        title = title_candidates[0]["text"]

    outline = []
    for h in headings:
        level = size_to_level.get(h["size"])
        if level:
            outline.append({
                "level": level,
                "text": h["text"],
                "page": h["page"]
            })

    print(f"Extracted title: {title}")
    print(f"Found {len(outline)} heading(s)")
    return {
        "title": title,
        "outline": outline
    }

def process_pdfs():
    input_dir = Path(r"C:\Users\admin\Desktop\Adobe\input")
    output_dir = Path(r"C:\Users\admin\Desktop\Adobe\output")
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))
    print(f"Searching in: {input_dir}")
    print(f"PDF files found: {len(pdf_files)}")

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        result = extract_headings_from_pdf(pdf_file)
        output_path = output_dir / f"{pdf_file.stem}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Saved output to: {output_path}")

if __name__ == "__main__":
    print("Script started")
    process_pdfs()
    print("Script finished")
