from .types.chat import (
    ChatCompletion,
    Choice,
    ChatCompletionMessage,
    ChatCompletionMessageToolCall,
    Function,
)


class _Completions:
    def create(self, **kwargs):
        raise NotImplementedError("OpenAI API is not available in this environment")


class _Chat:
    def __init__(self):
        self.completions = _Completions()


class OpenAI:
    def __init__(self):
        self.chat = _Chat()


__all__ = [
    "OpenAI",
    "ChatCompletion",
    "Choice",
    "ChatCompletionMessage",
    "ChatCompletionMessageToolCall",
    "Function",
]
