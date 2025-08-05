from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tavily = TavilySearchResults(max_results = 2)
    tools = [tavily]

    return tools

def create_tool_node(tools):
    """
    Creates and returns a toolnode for the graph
    """

    return ToolNode(tools = tools)