# 🤖 Gemini Chatbot — Assistente pessoal

Chatbot desenvolvido com Python, utilizando [Streamlit](https://streamlit.io/) para a interface web e a API do [Google Gemini](https://aistudio.google.com/app/apikey) para geração de respostas com inteligência artificial, mantendo o histórico da conversa de forma contínua.

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- google-genai (SDK oficial do Gemini)
- python-dotenv

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/JosielJrr/chatbot-gemini.git
cd chatbot-gemini
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o `.env`:

Use o comando abaixo para criar um arquivo `.env` com base no modelo:

```bash
cp .env.example .env
```

Em seguida, abra o arquivo `.env` e insira a sua chave de API do Google Gemini.

## ▶️ Como executar

Inicie a aplicação com o comando:

```bash
streamlit run main.py
```

## 📌 Observação

Para que a aplicação funcione corretamente, é necessário possuir uma **chave de API válida do Google Gemini**. O arquivo `.env.example` fornece orientações para obtê-la e adicioná-la ao projeto.
> 🚀 **Deploy:** [Acesse o chatbot online aqui](https://chatbot-gemini-nmxvt6umm4efyusmvyjza7.streamlit.app/)
