import streamlit as st
from groq import Groq

# Title of the app
st.title("AI Chatbot")

# Input box
user_input = st.text_input("Ask something:")

# Create Groq client
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# If user enters something
if user_input:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content

    st.write("Bot:", reply)