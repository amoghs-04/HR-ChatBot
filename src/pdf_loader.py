import pdfplumber

def load_pdf(pdf_path):
    """
    Extract text and page numbers from PDF.
    """

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_num, page in enumerate(pdf.pages, start=1):

            text = page.extract_text()

            if text:

                pages.append({
                    "page": page_num,
                    "text": text
                })

    return pages