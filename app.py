import os

import streamlit as st

from chains import load_chain
from memory import load_memory

st.set_page_config(layout='wide')
st.title('💬 Law Chatbot')

uploaded_file = st.file_uploader('Choose a file', type=['txt', 'pdf'])

if uploaded_file is not None:
    with open(uploaded_file.name, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    chain = load_chain(uploaded_file.name, uploaded_file.type)
    st.write('## 🤖 We are ready to answer your questions!')
    memory = load_memory(st)

    if question := st.chat_input():
        st.session_state.messages.append({'role': 'user', 'content': question})
        st.chat_message('user').write(question)

        response = chain.invoke(
            {
                'input': question,
                'chat_history': memory.load_memory_variables({})['history'],
            },
        )
        answer = response['answer']
        st.session_state.messages.append(
            {'role': 'assistant', 'content': answer},
        )
        st.chat_message('assistant').write(answer)
