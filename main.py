import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_apikey"])

st.set_page_config(page_title="Greg the Bot", page_icon="🤖", layout="wide")
st.title('Ask Greg')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input('Message Greg...')

if prompt:
    # display prompt
    st.chat_message('user').markdown(prompt)
    # store user prompt in state
    st.session_state.messages.append({'role':'user', 'content':prompt})
    # send prompt to LLM
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                'role': 'system',
                'content': 'You are a helpful assistant named Greg. You are tasked with answering questions from the user. Be polite and friendly.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    response = completion.choices[0].message.content
    # show LLM response
    st.chat_message('assistant').markdown(response)
    # store LLM response in state
    st.session_state.messages.append({'role':'assistant', 'content':response})