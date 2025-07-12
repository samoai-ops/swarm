from ..base import BaseModelV2 as BaseModel

class Function(BaseModel):
    name: str
    arguments: str

class ChatCompletionMessageToolCall(BaseModel):
    id: str
    type: str
    function: Function
