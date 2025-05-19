from pdf2image import convert_from_path
import pytesseract

custom_config = r'--oem 3 --psm 4'

def extract_text_from_pdf(file_path):
    pages = convert_from_path(file_path, 300)  # Converts PDF to images
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page, config=custom_config)  # OCR the image
    return text