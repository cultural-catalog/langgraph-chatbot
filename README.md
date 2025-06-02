# LangGraph Stateless Chatbot

A minimal stateless chatbot using LangGraph and Ollama with a `get_current_time` tool.

## Setup

1. **Install Ollama**:
   - Follow instructions at https://ollama.com/ to install Ollama.
   - Pull the LLaMA 3.2 model:
     ```bash
     ollama pull llama3.2

2. Ensure Ollama is running on the default port (11434):
    ```bash
    ollama serve
    ```

3. Set up the Python environment:
    ```bash
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```

4. Run the chatbot:
    ```bash

    python chatbot.py
    ```

## Program Output

<pre>
(myvenv) MacBook-Air:langgraph-chatbot anish$ python chatbot.py 
/Users/anish/anish7605/github-projects/langgraph-chatbot/chatbot.py:20: LangChainDeprecationWarning: The class `Ollama` was deprecated in LangChain 0.3.1 and will be removed in 1.0.0. An updated version of the class exists in the :class:`~langchain-ollama package and should be used instead. To use it run `pip install -U :class:`~langchain-ollama` and import as `from :class:`~langchain_ollama import OllamaLLM``.
  llm = Ollama(model="llama3.1")
Chatbot started. Type 'exit' to quit.
You: What time is it?
Bot: The current time is 2025-05-30T19:25:35.778998+00:00 (UTC).
You: exit
(myvenv) MacBook-Air:langgraph-chatbot anish$ 
</pre>
