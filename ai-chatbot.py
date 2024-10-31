import streamlit as st
import requests
import json

# Set up Streamlit page layout
st.set_page_config(page_title="Llama Chatbot", layout="wide")
st.title("Chat with Llama")

# Initialize session state for storing conversation
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

# User input
question = st.text_input("Ask me a question (type 'exit' to quit):")

# If user enters a question
if question:
    # If user types 'exit', end the conversation
    if question.lower() == "exit":
        st.write("Goodbye!")
    else:
        # Data payload for API request
        data = {
            'model': 'llama3.1',
            'messages': [{'role': 'user', 'content': question}],
            'stream': False
        }
        url = 'http://localhost:11434/api/chat'

        # Make request to API
        response = requests.post(url, json=data)
        response_json = json.loads(response.text)
        ai_reply = response_json['message']['content']

        # Display response in Streamlit and update conversation history
        st.session_state.conversation.append({"user": question, "ai": ai_reply})

        # Display the full conversation history
        for msg in st.session_state.conversation:
            st.write("**You:**", msg["user"])
            st.write("**Llama:**", msg["ai"])

# Run Streamlit app from the terminal
# Command: streamlit run chatbot_app.py
