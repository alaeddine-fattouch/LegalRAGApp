
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

contextualize_q_system_prompt = (
    'Given a conversation history and the latest user question, '
    'which may refer to context in the conversation history, '
    'formulate a standalone question that can be understood '
    'without the conversation history. DO NOT answer the question, '
    'rephrase it if necessary, otherwise return it as is.'
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', contextualize_q_system_prompt),
        MessagesPlaceholder('chat_history'),
        ('human', '{input}'),
    ],
)

legal_q_system_prompt = (
    'You are a legal expert specializing in law. Using the provided legal excerpts {context}, '
    'answer the question. If relevant legal texts are not included or if the request is not related to Tunisian law, '
    'indicate that you do not have the necessary references to answer and therefore cannot provide a response. '
    'To the extent possible, answer the question with the available information. Be as detailed as necessary in your response. '
    'If you cannot answer the question, explain why.'
)

legal_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', legal_q_system_prompt),
        MessagesPlaceholder('chat_history'),
        ('human', '{input}'),
    ],
)
