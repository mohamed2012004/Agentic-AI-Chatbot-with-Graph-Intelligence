from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """A node representing a basic chatbot in the graph."""
    def __init__(self, model):
        self.llm=model
    
    def process(self,state:State)-> dict:
        """Process the state and return a response from the chatbot.""" 
        return {"messages": self.llm.invoke(state["messages"])}   