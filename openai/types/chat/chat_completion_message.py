from dataclasses import dataclass
from typing import List, Optional
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall

@dataclass
class ChatCompletionMessage:
    role: str
    content: str
    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None

    def model_dump_json(self) -> str:
        """Return a JSON representation of the message."""
        import json
        from dataclasses import asdict

        return json.dumps(asdict(self))
