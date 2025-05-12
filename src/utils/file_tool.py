from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(file_path):
    pages = convert_from_path(file_path, 300)  # Converts PDF to images
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)  # OCR the image
    return text