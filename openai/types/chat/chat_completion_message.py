from dataclasses import dataclass, field
from typing import List, Optional
import json
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall

@dataclass
class ChatCompletionMessage:
    role: str
    content: Optional[str] = None
    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None
    function_call: Optional[dict] = None
    sender: Optional[str] = None

    def model_dump_json(self) -> str:
        return json.dumps({
            "role": self.role,
            "content": self.content,
            "tool_calls": [tc.as_dict() for tc in self.tool_calls] if self.tool_calls else None,
            "function_call": self.function_call,
            "sender": self.sender,
        })
