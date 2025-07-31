import os
import streamlit as st
from langchain_groq import ChatGroq
from src.langgraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            if groq_api_key == "" and os.environ["GROQ_API_KEY"] == "":
                st.error("Please enter the Groq API key")

            llm = ChatGroq(api_key= "GROQ_API_KEY", model= "selected_groq_model")

        except Exception as e:
            raise ValueError (f"Error Occured With Exception: {e}")
        return llm