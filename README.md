# LegalRAG

A Streamlit application for querying legal documents using RAG.
## Live Demo

[LegalRAG App](https://legalragapp-knowdroids-assessment.streamlit.app/)

## Features

- Document upload (PDF, TXT)
- Chat interface for document queries
- RAG-based responses
- Conversation memory
- Semantic search

## Technical Implementation

- RAG Pipeline with document chunking and retrieval
- PDF and TXT document processing
- ChromaDB vector store
- Streamlit web interface
- GitHub Actions CI/CD
- Docker containerization
- Type hints and mypy integration

## Prerequisites

- Python 3.11

## Running Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/LegalRAGApp.git
cd LegalRAGApp
```

2. Install dependencies using uv:
```bash
pip install uv && uv sync
```

3. Start the application:
```bash
uv run streamlit run app.py
```

4. Open your web browser and navigate to `http://localhost:8501`

5. Upload a legal document (PDF or TXT format)

6. Start asking questions about the document content


## Development

- Pre-commit hooks for code quality
- Type checking with mypy
- GitHub Actions workflow for:
  - Code quality checks
  - Docker image building
  - Image pushing to DockerHub

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
