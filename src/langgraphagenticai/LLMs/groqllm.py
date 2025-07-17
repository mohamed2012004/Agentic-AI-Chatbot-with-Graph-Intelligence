import streamlit as st
import os
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
        self.groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "")
    def get_llm_model(self):
        try:
            groq_api_key = self.groq_api_key
            selected_groq_model = self.user_controls_input["selected_groq_model"]    
            if not groq_api_key:
                st.error("⚠️ Please enter your GROQ API key ")
            llm=ChatGroq(api_key=groq_api_key, model=selected_groq_model)    
        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")
        return llm