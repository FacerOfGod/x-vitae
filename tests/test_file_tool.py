
from reportlab.pdfgen import canvas
import pytest
from src.utils.file_tool import *

@pytest.fixture
def test_pdf_file(tmp_path):
    #file_path = "src/ressources/cv.pdf"
    file_path = "src/ressources/test_file.pdf"

    #create_test_pdf(file_path)
    yield file_path

def create_test_pdf(filename):
    c = canvas.Canvas(str(filename))
    c.drawString(100, 750, "This is a test PDF file.")
    c.drawString(100, 730, "It contains a couple of lines of text.")
    c.drawString(100, 710, "You can use this file to test your PDF text extraction.")
    c.save()

def test_pdf_text_extraction(test_pdf_file):
    expected_lines = [
        "This is a test PDF file.",
        "It contains a couple of lines of text.",
        "You can use this file to test your PDF text extraction."
    ]
    text = extract_text_from_pdf(str(test_pdf_file))
    print(text)
    for line in expected_lines:
        assert line in text
