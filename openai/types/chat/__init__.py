from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ChatCompletionMessage:
    role: str
    content: Optional[str] = None
    function_call: Optional[dict] = None
    tool_calls: Optional[List['ChatCompletionMessageToolCall']] = None
    # custom attribute for sender used in tests
    sender: Optional[str] = None

    def model_dump_json(self) -> str:
        """Mimic the pydantic model_dump_json method used in tests."""
        from dataclasses import asdict
        import json
        return json.dumps(asdict(self))

from .chat_completion_message_tool_call import ChatCompletionMessageToolCall, Function
from .chat_completion import ChatCompletion, Choice

__all__ = [
    'ChatCompletionMessage',
    'ChatCompletionMessageToolCall',
    'Function',
    'ChatCompletion',
    'Choice',
]
