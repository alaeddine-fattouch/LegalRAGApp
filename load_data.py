from __future__ import annotations

from langchain.schema import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader


def load_text_file(file_path: str, encoding: str = 'utf-8') -> Document:
    """ Loads a text file and returns a Document object.

    Args:
        file_path: path of the text file.
        encoding: encoding of the text file (default: 'utf-8')

    Returns:
        A Document object.
    """
    loader = TextLoader(file_path, encoding=encoding)
    return loader.load()[0]


def load_pdf_file(file_path: str) -> list[Document]:
    """ Loads a pdf file and returns a list of Document objects.

    Args:
        file_path: path of the pdf file.

    Returns:
        A list of Document objects.
    """
    loader = PyPDFLoader(file_path)
    return loader.load()
