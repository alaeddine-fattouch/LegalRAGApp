from __future__ import annotations

from typing import List

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from load_data import load_pdf_file
from load_data import load_text_file


def create_index(docs: list[Document]) -> Chroma:
    """Creates a vectorstore index from a list of Document objects.

    Args:
        docs: List of Document objects.

    Returns:
        A Chroma vectorstore instance that can be used for similarity search.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name='nlpaueb/legal-bert-base-uncased',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True},
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    split_docs = text_splitter.split_documents(docs)

    vector_store = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory='chroma_db',
        collection_name='legal_docs',
    )
    vector_store.persist()

    return vector_store
