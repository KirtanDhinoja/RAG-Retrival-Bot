import streamlit as st
from graph import rag_app

st.set_page_config(page_title="Agentic AI Chat", page_icon="🤖")
st.title(" Agentic AI eBook Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about Agentic AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    result = rag_app.invoke({"question": prompt})
    
    with st.chat_message("assistant"):
        st.markdown(result["answer"])
        with st.expander("Retrieved Context"):
            st.write(result["context"])

    st.session_state.messages.append({"role": "assistant", "content": result["answer"]})