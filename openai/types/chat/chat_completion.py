from ..base import BaseModelV2 as BaseModel
from typing import List
from . import ChatCompletionMessage

class Choice(BaseModel):
    message: ChatCompletionMessage
    finish_reason: str
    index: int

class ChatCompletion(BaseModel):
    id: str
    created: int
    model: str
    object: str
    choices: List[Choice]
