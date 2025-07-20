from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state_chatbot import State
from src.langgraphagenticai.state.state_chatbot_with_tool import StateTool
from src.langgraphagenticai.state.state_ai_news import StateNews 
from src.langgraphagenticai.nodes.report_chatbot_node import ReportChatbotNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode




class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder =""
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph to generate report.
        
        """
        self.graph_builder=StateGraph(State)
    

        Chatbot = ReportChatbotNode(self.llm)
        self.graph_builder.add_node("orchestrator", Chatbot.orchestrator)
        self.graph_builder.add_node("llm_call", Chatbot.llm_call)
        self.graph_builder.add_node("synthesizer", Chatbot.synthesizer)
        self.graph_builder.add_edge(START, "orchestrator")
        self.graph_builder.add_conditional_edges(
        "orchestrator", Chatbot.assign_workers, ["llm_call"]
            )

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
    
    
    def ai_news_builder_graph(self):  
        
        
        ai_node=AINewsNode(self.llm)
        self.graph_builder=StateGraph(StateNews)
        
        self.graph_builder.add_node("fetch_news",ai_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_node.summarize_news)
        self.graph_builder.add_node("save_results", ai_node.save_result)
        
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_results")
        self.graph_builder.add_edge("save_results", END)  
    
    
    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Report Chatbot":
            self.basic_chatbot_build_graph()
        
        if usecase == "Chatbot With Web":
             self.chatbot_with_tools_build_graph()
             
        if usecase == "AI News":
            self.ai_news_builder_graph()         
        return self.graph_builder.compile()

