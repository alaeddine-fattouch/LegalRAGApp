from __future__ import annotations

from pathlib import Path

from load_data import load_pdf_file
from load_data import load_text_file


def test_loaders():
    text_file = Path('test_files/sample.txt')
    text_file.parent.mkdir(exist_ok=True)

    with open(text_file, 'w', encoding='utf-8') as f:
        f.write('This is a test document.\nIt has multiple lines.\n')

    print('\nLoading text file:')
    text_doc = load_text_file(str(text_file))
    print(f'Text content: {text_doc.page_content}')
    print(f'Metadata: {text_doc.metadata}')

    pdf_file = Path('test_files/sample.pdf')
    pdf_file.parent.mkdir(exist_ok=True)

    if pdf_file.exists():
        print('\nLoading PDF file:')
        pdf_docs = load_pdf_file(str(pdf_file))
        for i, doc in enumerate(pdf_docs):
            print(f'\nPage {i + 1}:')
            print(f'Content: {doc.page_content[:200]}...')
            print(f'Metadata: {doc.metadata}')
    else:
        print(f'\nPDF file not found at {pdf_file}')
        print('Please add a PDF file to test the PDF loader')


if __name__ == '__main__':
    test_loaders()
