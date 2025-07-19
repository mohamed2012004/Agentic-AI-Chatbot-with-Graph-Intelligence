import streamlit as st

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        if self.usecase == "Basic Chatbot":
            state = self.graph.invoke({"topic": self.user_message})
            if "final_report" in state:
                st.chat_message("user").write(self.user_message)
                st.chat_message("assistant").markdown(state["final_report"])
            else:
                st.warning("No 'final_report' found in the state.")
