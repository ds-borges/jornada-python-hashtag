import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_openai_work:bool=True
if api_openai_work:
    api_key_agent= os.getenv("OPENAI_API_KEY")
else:
    api_key_agent= os.getenv("GEMINI_API_KEY")

if api_openai_work:
    model = OpenAI(
        api_key=api_key_agent    
    )
else:
    model = OpenAI(
        api_key=api_key_agent,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

st.write("Chatboot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []


input_user = st.chat_input("Digite sua mensagem")

if input_user:
    #Salvando a mensagem do usuário
    mensagem_user = {"role": "user", "content": input_user}
    st.session_state["lista_mensagens"].append(mensagem_user)
    

    if api_openai_work:
        #Criando a resposta da IA
        output_ia = model.chat.completions.create(
            #messages = st.session_state["lista_mensagens"],
            messages=[{"role": "user", "content": "Olá, funciona?"}],
            model="gpt-3.5-turbo"
        )
    else:
        output_ia = model.chat.completions.create(
            model="gemini-2.0-flash",
            messages = st.session_state["lista_mensagens"]
        )
    print(f"\n{output_ia.choices[0].message.content}\n")

    #Salvando a mensagem da IA
    mensagem_ia = {"role": "assistant", "content": output_ia.choices[0].message.content}
    st.session_state["lista_mensagens"].append(mensagem_ia)

    #print(st.session_state["lista_mensagens"])
    for mensagem in st.session_state["lista_mensagens"]:
        role = mensagem["role"]
        texto = mensagem["content"]
        st.chat_message(role).write(texto)
