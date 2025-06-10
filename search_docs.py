from __future__ import annotations

from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from index_data import create_index
from load_data import load_pdf_file
from load_data import load_text_file


def search_legal_docs(
    query: str,
    file_paths: list[str],
    k: int = 4,
) -> list:
    """Search through legal documents for relevant information.

    Args:
        query: The search query
        file_paths: List of paths to legal documents
        k: Number of results to return

    Returns:
        List of relevant document chunks
    """
    documents = []
    for file_path in file_paths:
        path = Path(file_path)
        if path.suffix.lower() == '.pdf':
            docs = load_pdf_file(str(path))
            documents.extend(docs)
        elif path.suffix.lower() == '.txt':
            doc = load_text_file(str(path))
            documents.append(doc)

    vector_store = create_index(documents)
    return vector_store.similarity_search(query, k=k)


def main():
    test_files = [
        'test_files/sample.txt',
        'test_files/sample.pdf',
    ]

    results = search_legal_docs(
        'What are the payment terms?',
        test_files,
    )

    for doc in results:
        print('\nRelevant chunk:')
        print(doc.page_content)
        print(f'Source: {doc.metadata.get("source", "Unknown")}')


if __name__ == '__main__':
    main()
