
from PyPDF2 import PdfReader
from docx import Document

def parse_resume(file):
    """
    Extracts text from a given resume file (PDF or DOCX).
    """
    try:
        # Process PDF files
        if file.filename.endswith(".pdf"):
            reader = PdfReader(file)
            extracted_text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
            
            if not extracted_text.strip():
                raise ValueError("The uploaded PDF contains no readable text.")
            
            return extracted_text

        # Process DOCX files
        elif file.filename.endswith(".docx"):
            doc = Document(file)
            extracted_text = " ".join(para.text for para in doc.paragraphs if para.text)
            
            if not extracted_text.strip():
                raise ValueError("The uploaded DOCX file contains no readable text.")
            
            return extracted_text

        # Unsupported file format
        else:
            raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

    except Exception as e:
        return f"Error: Unable to process the file. {str(e)}"
