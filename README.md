# streamlit-ai-chatbot
# Llama Chatbot App

A simple chatbot app built with Streamlit that uses the Llama model API, hosted through [Ollama](https://ollama.com), to generate responses. Users can interact with the chatbot directly in the browser, making it a quick and interactive way to experience conversational AI.

## Features
- **Live Chat**: Send questions to the chatbot and receive responses in real-time.
- **Conversation History**: See the full conversation history for easy reference.
- **Exit Option**: Type "exit" to end the conversation.

## Requirements
- **Python 3.7+**
- **Ollama**: For hosting the Llama model API locally.
- **Streamlit**: For running the web interface.
- **requests** library: For making API requests.

## Setup Instructions

### 1. Install Ollama

Visit the [Ollama download page](https://ollama.com/download) and follow the instructions for your operating system to install Ollama.

### 2. Add the Llama Model to Ollama

Once Ollama is installed, pull the Llama model to use in the chatbot app:

```bash
ollama pull llama3.1
```

This will download the Llama model, making it available to serve locally.

### 3. Start the Llama Model API in Ollama

To start the Llama model API locally, run the following command:

```bash
ollama serve llama3.1
```

This will host the Llama model API on `localhost:11434` by default, ready to accept requests from the Streamlit app.

### 4. Clone the Repository

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yourusername/llama-chatbot-app.git
cd llama-chatbot-app
```

### 5. Install Python Dependencies

Install the required Python libraries using pip:

```bash
pip install streamlit requests
```

### 6. Verify API URL in Code

The chatbot app is set up to connect to the Llama model API running on `http://localhost:11434`. Verify the `url` in `chatbot_app.py` if needed:

```python
url = 'http://localhost:11434/api/chat'
```

## Running the App

To start the chatbot app, use the following command:

```bash
streamlit run chatbot_app.py
```

After running the command, you should see output similar to this:

```bash
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
```

Visit `http://localhost:8501` in your browser to interact with the chatbot.

## Usage

1. **Ask a Question**: Type a question in the input box and press Enter. The chatbot will respond in real-time.
2. **Exit the Chat**: To end the chat, type "exit" in the input box.
3. **Review History**: The conversation history is displayed for easy reference.

## Example

```
You: What is the capital of France?
Llama: The capital of France is Paris.

You: Who wrote "Pride and Prejudice"?
Llama: "Pride and Prejudice" was written by Jane Austen.

You: exit
Goodbye!
```

## Customization

You can customize the chatbot appearance, add custom styling, or change the response formatting in `chatbot_app.py`.

## Troubleshooting

- **Error Connecting to API**: Ensure Ollama is running the Llama model API on `localhost:11434` by verifying the output of `ollama serve llama3.1`. You may need to update `url` in `chatbot_app.py` if the API is hosted on a different port or server.

## License

This project is open-source and available under the MIT License.
