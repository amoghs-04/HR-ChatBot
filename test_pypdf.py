from PyPDF2 import PdfReader

reader = PdfReader("data/HR-Policy-Manual-Template.pdf")

print("Pages:", len(reader.pages))

text = reader.pages[0].extract_text()

print("\nTEXT:\n")
print(text)