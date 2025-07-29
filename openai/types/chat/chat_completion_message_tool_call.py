from dataclasses import dataclass

@dataclass
class Function:
    name: str
    arguments: str

@dataclass
class ChatCompletionMessageToolCall:
    id: str
    type: str
    function: Function
