import json
from datetime import datetime, timezone
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.llms import Ollama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Define the state
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Define the get_current_time tool
def get_current_time() -> dict:
    """Return the current UTC time in ISO-8601 format.
    Example → {"utc": "2025-05-21T06:42:00Z"}"""
    return {"utc": datetime.now(timezone.utc).isoformat()}

# Initialize the LLM with Ollama
llm = Ollama(model="llama3.1")

# Define the chat node
def chat_node(state: State):
    messages = state["messages"]
    last_message = messages[-1].content.lower()
    
    try:
        # Check if the user is asking for the time
        if any(keyword in last_message for keyword in ["time is it", "what's the time", "current time"]):
            tool_result = get_current_time()
            response_content = f"The current time is {tool_result['utc']} (UTC)."
        else:
            # Normal LLM response for non-time queries
            response_content = llm.invoke(messages)
        
        return {"messages": [AIMessage(content=response_content)]}
    except Exception as e:
        return {"messages": [AIMessage(content=f"Error: {str(e)}")]}

# Build the graph
workflow = StateGraph(State)
workflow.add_node("chat", chat_node)
workflow.add_edge(START, "chat")
workflow.add_edge("chat", END)

# Compile the graph
app = workflow.compile()

# Main function to run the chat
def main():
    print("Chatbot started. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        state = {"messages": [HumanMessage(content=user_input)]}
        result = app.invoke(state)
        print("Bot:", result["messages"][-1].content)

if __name__ == "__main__":
    main()
