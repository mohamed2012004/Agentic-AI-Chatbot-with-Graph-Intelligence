import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        if self.usecase == "Report Chatbot":
            state = self.graph.invoke({"topic": self.user_message})
            if "final_report" in state:
                st.chat_message("user").write(self.user_message)
                st.chat_message("assistant").markdown(state["final_report"])
            else:
                st.warning("No 'final_report' found in the state.")
        elif self.usecase=="Chatbot With Web":
             # Prepare state and invoke the graph
            initial_state = {"messages": [self.user_message]}
            res = self.graph.invoke(initial_state)
            
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
        elif self.usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result=self.graph.invoke({"messages":[HumanMessage (content=frequency)]})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")                