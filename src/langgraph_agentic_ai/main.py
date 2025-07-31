import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMs.groq_llm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlit_ui.display_result import DisplayResultStreamlit

def load_langgraph_agentic_ai_app():
    """
    Loads and runs the LangGraph Agentic AI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up graph based on the selected use case, and displays the output while 
    implementing exception hangling for robustness. 
    """
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure the LLM
            obj_llm_config = GroqLLM(user_controls_input = user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("Error: LLM Model could not be initialized")
                return
            
            # Initialize and set up the graph based on use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: no usecase selected")
                return
            
            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph setup failed - {e}")
            return
