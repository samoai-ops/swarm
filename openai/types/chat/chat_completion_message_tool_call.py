class Function:
    def __init__(self, name: str = "", arguments: str = ""):
        self.name = name
        self.arguments = arguments


class ChatCompletionMessageToolCall:
    def __init__(self, id: str = "", type: str = "", function: Function | None = None):
        self.id = id
        self.type = type
        self.function = function or Function()
