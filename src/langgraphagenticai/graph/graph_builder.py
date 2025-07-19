from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state_chatbot import State
from src.langgraphagenticai.state.state_chatbot_with_tool import StateTool 
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder =""
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.graph_builder=StateGraph(State)
    

        Chatbot = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("orchestrator", Chatbot.orchestrator)
        self.graph_builder.add_node("llm_call", Chatbot.llm_call)
        self.graph_builder.add_node("synthesizer", Chatbot.synthesizer)
        self.graph_builder.add_edge(START, "orchestrator")
        self.graph_builder.add_conditional_edges(
        "orchestrator", Chatbot.assign_workers, ["llm_call"]
            )

# add_conditional_edges("orschestrator", assign_workers, ["llm_call"])
        self.graph_builder.add_edge("llm_call", "synthesizer")
        self.graph_builder.add_edge("synthesizer", END)
        
        
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        tools=get_tools()
        tool_node=create_tool_node(tools)
        
        llm=self.llm
        chatbot=ChatbotWithToolNode(llm)
        self.graph_builder=StateGraph(StateTool)
    
        
        self.graph_builder.add_node("chatbot",chatbot.create_chatbot(tools))
        self.graph_builder.add_node("tools", tool_node)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")    
        
    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        if usecase == "Chatbot With Web":
             self.chatbot_with_tools_build_graph()    
        return self.graph_builder.compile()

