import json

from .chat_completion_message_tool_call import ChatCompletionMessageToolCall, Function


class ChatCompletionMessage:
    def __init__(self, role: str, content: str = "", tool_calls=None, function_call=None):
        self.role = role
        self.content = content
        self.tool_calls = tool_calls
        self.function_call = function_call

    def model_dump_json(self):
        def serialize_tool_call(tc: ChatCompletionMessageToolCall):
            return {
                "id": tc.id,
                "type": tc.type,
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments,
                },
            }

        tool_calls = (
            [serialize_tool_call(tc) for tc in self.tool_calls]
            if self.tool_calls
            else None
        )

        return json.dumps(
            {
                "role": self.role,
                "content": self.content,
                "tool_calls": tool_calls,
            }
        )


class Choice:
    def __init__(self, message: ChatCompletionMessage, finish_reason: str = "stop", index: int = 0):
        self.message = message
        self.finish_reason = finish_reason
        self.index = index


class ChatCompletion:
    def __init__(self, id: str, created: int, model: str, object: str, choices: list[Choice]):
        self.id = id
        self.created = created
        self.model = model
        self.object = object
        self.choices = choices
