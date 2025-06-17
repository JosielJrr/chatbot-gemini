import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Instancia o cliente Gemini
cliente = genai.Client(api_key=api_key)
modelo = "gemini-2.0-flash"

# Configuração do chat com instrução de sistema
chat_config = types.GenerateContentConfig(
    system_instruction="Você é um assistente pessoal que responde sempre de forma sucinta.",
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

# Cria o chat se ainda não existir na sessão
if "chat" not in st.session_state:
    st.session_state.chat = cliente.chats.create(
        model=modelo,
        config=chat_config
    )

st.write("### 🤖 ChatBot + Gemini")

# Inicializa a lista de mensagens (só pra mostrar no front)
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Renderiza histórico na interface
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# Campo para entrada do usuário
prompt = st.chat_input("Pergunte alguma coisa...")

if prompt:
    # Exibe a mensagem do usuário
    st.chat_message("user").write(prompt)
    st.session_state["lista_mensagens"].append({"role": "user", "content": prompt})

    try:
        # Spinner enquanto a IA responde
        with st.spinner("Pensando..."):
            # Envia pro Gemini e obtém a resposta
            resposta_modelo = st.session_state.chat.send_message(prompt)
            resposta_ia = resposta_modelo.text

    except Exception as e:
        resposta_ia = "❌ Ocorreu um erro ao processar sua mensagem."
        print(f"[ERRO GEMINI] {e}")

    # Exibe a resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})
