import streamlit as st
from groq import Groq

# App title
st.title("Hey! I'm a Groq-powered AI chatbot. Ask me anything.")

# System prompt input
system_prompt = st.text_input(
    "System Prompt",
    "You are a helpful AI assistant."
)

# Initialize Groq client
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input box
user_input = st.chat_input("Ask something...")

# When user sends a message
if user_input:

    # Show user message
    st.chat_message("user").write(user_input)

    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Send conversation to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": system_prompt}]
        + st.session_state.messages
    )

    # Extract reply
    reply = response.choices[0].message.content

    # Display AI response
    with st.chat_message("assistant"):
        st.write(reply)

    # Store AI reply
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    #streamlit run app.py