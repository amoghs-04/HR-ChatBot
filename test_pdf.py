import pdfplumber

pdf_path = "data/HR-Policy-Manual-Template (1).pdf"

try:
    with pdfplumber.open(pdf_path) as pdf:
        print("Total Pages:", len(pdf.pages))

        first_page = pdf.pages[0]

        text = first_page.extract_text()

        print("\nTEXT FOUND:\n")
        print(text[:1000] if text else "NO TEXT FOUND")

except Exception as e:
    print("ERROR:", e)
