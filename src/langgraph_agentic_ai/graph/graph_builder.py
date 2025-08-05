from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agentic_ai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraph_agentic_ai.nodes.chatbot_with_tools import ChatbotWithToolsNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot using LangGraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up conditional and directed edges between nodes.
        The chatbot node is set as the entry point.
        """
        
        # Define the tools and ToolNode
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Define the LLM
        llm = self.llm

        # Define Chatbot node
        chatbot_with_tools_node = ChatbotWithToolsNode(llm)
        chatbot_node = chatbot_with_tools_node.create_chatbot(tools)

        # Build the graph
        self.graph_builder.add_node("chatbot with tools", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot with tools")
        self.graph_builder.add_conditional_edges("chatbot with tools", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot with tools")


    def setup_graph(self, usecase: str):
        """
        Sets up the graph for selected usecase.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()