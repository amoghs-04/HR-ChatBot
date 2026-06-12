from src.pdf_loader import load_pdf

pages = load_pdf("data/HR-Policy-Manual-Template.pdf")

print("Pages Extracted:", len(pages))

print("\nFirst Page:\n")
print(pages[0]["text"][:500])