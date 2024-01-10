from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


class PDFParser:
    def get_text_chunks(self, text):
        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
        )
        chunks = text_splitter.split_text(text)
        return chunks

    def parse(self, pdf):
        text = ""
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_chunks = self.get_text_chunks(text)
        return text_chunks
