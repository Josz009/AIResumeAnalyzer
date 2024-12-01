
from PyPDF2 import PdfReader
from docx import Document

def parse_resume(file):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)
    elif file.filename.endswith(".docx"):
        doc = Document(file)
        return " ".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format.")
