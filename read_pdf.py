from pypdf import PdfReader

def read_pdf(path: str):
        
    reader = PdfReader(path)
    res = ""
    for page in reader.pages:
        res += page.extract_text()
    return res