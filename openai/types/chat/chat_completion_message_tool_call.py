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

    def as_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "function": {"name": self.function.name, "arguments": self.function.arguments},
        }
