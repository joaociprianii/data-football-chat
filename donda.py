import streamlit as st
import donda_frun

st.title("Data Oracle")

# Configurar a chave da API
api_key = donda_frun.get_api_key()


# Inicializar histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar entrada do usuário
if prompt := st.chat_input("Ask me anything"):
    # Exibir mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obter a resposta do assistente
    with st.chat_message("assistant"):
        response = donda_frun.answer_question_with_glossary_and_data(
            question=prompt
        )
        # Garantir que `response` seja tratado como texto
        response_content = response.content if hasattr(response, 'content') else str(response)

        # Exibir a resposta do assistente
        st.markdown(response_content)
        st.session_state.messages.append({"role": "assistant", "content": response_content})
