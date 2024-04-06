from pypdf import PdfReader
from llama_parse import LlamaParse
import asyncio

def read_pdf(path: str):
    parser = LlamaParse(api_key='llx-UNeRjwphgBNvFTY2H63Hr9YnA0q98z5XTZpo33QJ5fx6hQaJ', result_type="markdown")
    documents = parser.load_data(path)
    return documents[0].text