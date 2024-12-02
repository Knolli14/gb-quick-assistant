from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents.base import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

from gb_assistant.params import *


def create_pdf_doc(game_file):
    ''' Loads a pdf and creates a Document '''
    filepath = os.path.join(RAW_DATA_PATH, game_file)

    # load pages into Documents
    pages = PyPDFLoader(filepath).load()

    # collect texts and merge to one Document
    game_doc = Document(
        page_content=" ".join([doc.page_content for doc in pages]),
        metadata={"title": game_file.strip(".pdf")}
    )

    print(game_file, "has been loaded into a Document")
    return game_doc


def create_splits(game_docs, chunk_size=512, chunk_overlap=32):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    splits = splitter.split_documents(game_docs)
    print("Game_docs splitted..")
    return splits



if __name__ == "__main__":

    doc = create_pdf_doc("catan.pdf")
    print(create_splits([doc])[2])
