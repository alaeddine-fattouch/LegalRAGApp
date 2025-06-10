import streamlit as st
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_mistralai import ChatMistralAI

from index_data import create_index
from load_data import load_pdf_file
from load_data import load_text_file
from prompts import contextualize_q_prompt
from prompts import legal_prompt


@st.cache_resource
def load_chain(file_name: str, file_type: str):
    if file_type == 'text/plain':
        docs = load_text_file(file_name)
    elif file_type == 'application/pdf':
        docs = load_pdf_file(file_name)
    else:
        st.write('File type is not supported!')
        st.stop()

    retriever = create_index(docs)

    llm = ChatMistralAI(model='mistral-large-latest')
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt,
    )

    question_answer_chain = create_stuff_documents_chain(llm, legal_prompt)

    rag_chain = create_retrieval_chain(
        history_aware_retriever, question_answer_chain,
    )

    return rag_chain
