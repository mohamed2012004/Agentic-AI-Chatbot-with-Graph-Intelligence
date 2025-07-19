from src.langgraphagenticai.state.state_chatbot_with_tool import StateTool
from langchain_core.messages import AIMessage


class ChatbotWithToolNode:
    def __init__(self, llm):
        self.llm = llm

    def create_chatbot(self, tools):
        """Returns a chatbot node with tool capabilities."""
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state: StateTool):
            """Handles the chatbot's processing with tools."""
            # Process the state and invoke the LLM with tools
            response=llm_with_tools.invoke(
                state["messages"]
            )
            return {"messages":response}
        return chatbot_node