from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents.base import Document
import os

from gb_assistant.params import *


def create_pdf_doc(game_file):

    filepath = os.path.join(RAW_DATA_PATH, game_file)

    # load pages in to Documents
    pages = PyPDFLoader(filepath).load()

    game_doc = Document(
        page_content=" ".join([doc.page_content for doc in pages]),
        metadata={"title": filepath.strip(".pdf")}
    )

    print(game_file, "has been loaded into a Document")
    return game_doc

if __name__ == "__main__":

    create_pdf_doc(RAW_DATA_PATH+"/catan.pdf")
