from PyPDF2 import PdfReader


class PDFTool:
    def extract_text(self, input_pdf):
        reader = PdfReader(input_pdf)
        text = ""
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n\n--- Page {i + 1} ---\n"
                text += page_text
        return text