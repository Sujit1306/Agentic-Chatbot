from src.langgraph_agentic_ai.state.state import State

class ChatbotWithToolsNode:
    """
    Chatbot logic enhanced with tool integration
    """
    def __init__(self, model):
        self.llm = model

    # def process(self, state:State)->dict:
    #     """
    #     Process the input and generate a response with tool integration.
    #     """
    #     user_input = state["messages"][-1] if state["messages"] else ""
    #     llm_response = self.llm.invoke([{"role":"user", "content": user_input}])

    #     # simulate the tool specific logic
    #     tool_response = f"Tool integration for: '{user_input}'"

    #     return {"messages": [llm_response, tool_response]}

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State)->dict:
            """
            Chatbot logic for processing the input state and returning a response
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node