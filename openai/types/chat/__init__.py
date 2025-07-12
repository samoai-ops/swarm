from ..base import BaseModelV2 as BaseModel
from typing import List, Optional
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall, Function

class ChatCompletionMessage(BaseModel):
    role: str
    content: str
    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None
    function_call: Optional[dict] = None
    sender: Optional[str] = None

from .chat_completion import ChatCompletion, Choice

__all__ = [
    "ChatCompletionMessage",
    "ChatCompletionMessageToolCall",
    "Function",
    "ChatCompletion",
    "Choice",
]
