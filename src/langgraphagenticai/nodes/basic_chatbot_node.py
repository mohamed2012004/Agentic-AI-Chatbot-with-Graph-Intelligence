from src.langgraphagenticai.state.state_chatbot import State, Section, Sections, WorkerState
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.constants import Send


class BasicChatbotNode:
    """A node representing a basic chatbot in the graph."""
    def __init__(self, model):
        self.llm=model
     
    def orchestrator(self,state: State):
        """Orchestrator that generates a plan for the report"""
    
        planner=self.llm.with_structured_output(Sections)
        
        report_sections = planner.invoke(
            [
            SystemMessage(content="Generate a plan for the report."),
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),
            ]
                                            )

        print("Report Sections:",report_sections)

        return {"sections": report_sections.sections}

    def llm_call(self,state: WorkerState):
        """Worker writes a section of the report"""

        # Generate section
        section = self.llm.invoke(
        [
            SystemMessage(
                content="Write a report section following the provided name and description. Include no preamble for each section. Use markdown formatting."
            ),
            HumanMessage(
                content=f"Here is the section name: {state['section'].name} and description: {state['section'].description}"
            ),
        ]
        )

        # Write the updated section to completed sections
        return {"completed_sections": [section.content]}

    def assign_workers(self,state: State):
        """Assign a worker to each section in the plan"""

        # Kick off section writing in parallel via Send() API
        return [Send("llm_call", {"section": s}) for s in state["sections"]]

    def synthesizer(self,state: State):
        """Synthesize full report from sections"""

        # List of completed sections
        completed_sections = state["completed_sections"]

        # Format completed section to str to use as context for final sections
        completed_report_sections = "\n\n---\n\n".join(completed_sections)

        return {"final_report": completed_report_sections}
