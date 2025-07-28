# 📄 Adobe Hackathon 2025 - Challenge 1a: PDF Processing Solution

## 🚀 Overview

This is a solution for **Challenge 1a** of the **Adobe India Hackathon 2025**. The challenge requires building a robust and efficient PDF processing pipeline that extracts **structured data** from PDFs and outputs the results in **JSON format**. The solution is **Dockerized** to ensure platform independence, reproducibility, and easy deployment.

---

## ✅ Features

- 📄 **PDF Input Support**: Processes local PDF documents.
- 🔍 **Text Extraction**: Uses `PyMuPDF` (`fitz`) for fast and accurate extraction.
- 🧠 **Data Parsing**: Custom parsing logic to extract:
  - Headings
  - Subheadings
  - Paragraphs
  - Tabular data
- 📦 **Structured JSON Output**: Each PDF results in a structured `.json` file.
- 🐳 **Dockerized**: Runs in a reproducible Python 3.10 Docker container.

---

## 🧠 Approach

The processing is done through the following pipeline:

1. **Read and Parse PDF**  
   Using `PyMuPDF`, the PDF is parsed page by page.

2. **Text Block Analysis**  
   Extracts blocks using `page.get_text("dict")` and analyzes fonts and bounding boxes to infer structure.

3. **Classification of Content**  
   Applies heuristics (font size, position) to classify content as:
   - `heading`
   - `subheading`
   - `paragraph`
   - `table` (if applicable)

4. **Structured Assembly**  
   Reassembles content into a clean hierarchical format stored as JSON.

5. **Output**  
   Saves each structured result as `output/{filename}.json`.

---

## 📂 Project Structure

├── input_pdfs/
│ └── sample.pdf
├──  output/
│ └── sample.json
├── Dockerfile
├── process_pdf.py

📚 Dependencies
-Python 
-PyMuPDF (fitz)
-Docker (build & run)

👨‍💻 Developed By
Team Leader: [Prateek Singh Rajawat]
Hackathon Team: [Runtime Code Blockers]
Organization: Adobe Hackathon