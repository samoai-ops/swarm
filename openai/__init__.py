from types import SimpleNamespace

class OpenAI:
    def __init__(self):
        # minimal stub client
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=lambda **kwargs: None))
