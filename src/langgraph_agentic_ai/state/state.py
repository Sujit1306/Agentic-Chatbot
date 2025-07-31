from typing_extensions import TypedDict, Annotated, List
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the structure of state used in graph
    """
    messages: Annotated[List, add_messages]