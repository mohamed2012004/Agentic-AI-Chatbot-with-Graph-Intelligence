from typing_extensions import TypedDict
from langgraph.graph.message  import add_messages
from typing import Annotated
from typing import List
from pydantic import BaseModel, Field
import operator

# class State(TypedDict):
#     """
#     Represents the  structure  of the state used in graph
#     """
#     messages:Annotated[list,add_messages]

class Section(BaseModel):
    name:str=Field(description="Name for this section of the report")
    description:str=Field(description="Brief Overview of the main topics and concepts of the section")

class Sections(BaseModel):
    sections:List[Section]=Field(
        description="Sections of the report"
    )

class State(TypedDict):
    topic: str  # Report topic
    sections: list[Section]  # List of report sections
    completed_sections: Annotated[
        list, operator.add
    ]  # All workers write to this key in parallel
    final_report: str  # Final report

# Worker state
class WorkerState(TypedDict):
    section: Section
    completed_sections: Annotated[list, operator.add]
    