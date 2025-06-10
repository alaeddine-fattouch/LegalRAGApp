import streamlit as st
from langchain_core.memory import BaseMemory
from langchain_core.messages import HumanMessage, AIMessage
from typing import Any, Dict, List
from pydantic import Field


class ConversationWindowMemory(BaseMemory):
    """Memory that keeps a window of the conversation history."""

    k: int = Field(default=5, description="Number of messages to keep in memory")
    chat_memory: List[Any] = Field(default_factory=list, description="List of messages in memory")
    memory_key: str = Field(default="history", description="Key to use for memory variables")
    output_key: str = Field(default="answer", description="Key to use for output")

    @property
    def memory_variables(self) -> List[str]:
        """Return the list of memory variables."""
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Return history of the conversation."""
        return {self.memory_key: self.chat_memory[-self.k:] if self.chat_memory else []}

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, Any]) -> None:
        """Save the context of the conversation."""
        if self.output_key in outputs:
            self.chat_memory.append(HumanMessage(content=inputs["input"]))
            self.chat_memory.append(AIMessage(content=outputs[self.output_key]))

    def clear(self) -> None:
        """Clear memory contents."""
        self.chat_memory = []


def load_memory(st):
    """Loads the conversation memory.

    Args:
        st: Streamlit session state

    Returns:
        A ConversationWindowMemory instance
    """
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    memory = ConversationWindowMemory(k=5)

    for message in st.session_state.messages:
        if message['role'] == 'user':
            memory.chat_memory.append(HumanMessage(content=message['content']))
        else:
            memory.chat_memory.append(AIMessage(content=message['content']))

    return memory
