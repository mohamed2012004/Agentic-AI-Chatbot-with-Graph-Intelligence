from typing_extensions import TypedDict 
from langgraph.graph.message import add_messages,BaseMessage
from typing import Annotated, List

class StateTool(TypedDict):
    """
    Represents the structure of the state used in the chatbot graph.
    """
    messages: Annotated[List, add_messages]  # List of messages in the conversation