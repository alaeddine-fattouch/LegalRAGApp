from __future__ import annotations

from typing import List

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from load_data import load_pdf_file
from load_data import load_text_file


def create_index(docs: list[Document]) -> Chroma:
    """Creates a vectorstore index from a list of Document objects.

    Args:
        docs: List of Document objects.

    Returns:
        A Chroma vectorstore instance that can be used for similarity search.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    splits = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name='BAAI/bge-base-en-v1.5',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True},
    )

    vector_store = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory='chroma_db',
    )

    return vector_store
