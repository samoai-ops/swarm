from dataclasses import dataclass
from typing import List
from . import ChatCompletionMessage

@dataclass
class Choice:
    message: ChatCompletionMessage
    finish_reason: str
    index: int

@dataclass
class ChatCompletion:
    id: str
    created: int
    model: str
    object: str
    choices: List[Choice]
