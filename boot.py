import streamlit as st
import openai
import os


# Título da seção lateral
st.title('Aplicativo de Perguntas e Respostas para resolução de problemas')

st.markdown("Redes Sociais")

# Links das redes sociais
whatsapp = 'https://wa.me/5582981090042'
linkedin = 'https://www.linkedin.com/in/williamsrodrigues/'

# Criando botões lado a lado usando colunas
col1, col2 = st.columns(2)

with col1:
    if st.button('WhatsApp', key='whatsapp',icon='📱'):
        st.write(f'<a href="{whatsapp}" target="_blank">Abrindo WhatsApp...</a>', unsafe_allow_html=True)

with col2:
    if st.button('LinkedIn', key='linkedin',icon='🔗'):
        st.write(f'<a href="{linkedin}" target="_blank">Abrindo LinkedIn...</a>', unsafe_allow_html=True)


openai.api_key = os.getenv("OPENAI_API_KEY")  # Certifique-se de configurar a variável de ambiente com a sua chave

# Definindo a chave de API de forma segura (usando variáveis de ambiente)
openai.api_key = "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"

# Função para gerar resposta usando a nova interface da OpenAI
def generate_response(prompt):
    try:
        # Usando a nova API de chat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Você pode usar "gpt-4" se tiver acesso
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,  # Limite de tokens para a resposta
            temperature=0.7,  # Define a criatividade da resposta (0.0 a 1.0)
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

# Interface do Streamlit
st.image('problem.png', width=800)


# Campo de entrada para o usuário
prompt = st.text_input('Digite sua pergunta:', '')

# Botão de envio
if st.button('Enviar'):
    if prompt:
        # Gerar e exibir a resposta do chatbot
        response = generate_response(prompt)
        st.write('Resposta do Chatbot:', response)
    else:
        st.write('Por favor, insira uma pergunta.')
        st.balloons()


# Botão de ajuda
if st.button('Ajuda'):
    whatsapp = 'https://wa.me/5582981090042'
    st.write('Se precisar de ajuda, entre em contato com o suporte no WhatsApp:')
    st.markdown(f'[Me chama no WhatsApp]({whatsapp})')

# Organizar todos os botões
st.markdown('<style>div.stButton>button {width: 100%}</style>', unsafe_allow_html=True)
        
# Usando markdown para incorporar o vídeo com iframe
st.video('https://www.youtube.com/watch?v=D0O-Lk_Dnkw')


#Resumo sobre o projeto
st.header("Resumo sobre o projeto")

st.markdown("""
> **Projeto:** 
> O projeto consiste em um aplicativo de perguntas e respostas para resolução de problemas.


> **Objetivo:** 
> O objetivo do projeto é ajudar os usuários a resolver problemas de forma mais eficiente e eficaz.
            

> **Funcionalidades:**
> - Gerar Perguntas e respostas para auxiliar os usuários a encontrar possiveis problemas em suas áreas de atuação.
            
> **Tecnologias Utilizadas:**
> - Streamlit
> - OpenAI GPT API

> **Desenvolvido por:**
> - Williams Rodrigues 

> **Parceiria com:**
> - Claudio Alexandre

> **Contato:**
> - WhatsApp: [Clique aqui](https://wa.me/5582981090042)
> - LinkedIn: [Clique aqui](https://www.linkedin.com/in/williamsrodrigues/)

> **Qualificação:**
> - Pós Graduado em Ciência de Big Date Analytics
> - Bacharel em Administração de empresas
            
> **Especialidade:**
> - Desenvolvimento e Analise de Dados com Python e Power BI
> - Desenvolvimento de Aplicações Web com Python e Streamlit
> - Soluções de Desenvolvimento para acompanhamento de Processos
> - Desenvolvimento APP Mobile para Registro e suas aplicações no dia a dia      
> - Melhoria Continua do Processo
> - Implementações de Processos de Qualidade


           

""")





