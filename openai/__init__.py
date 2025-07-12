from types import SimpleNamespace

class OpenAI:
    def __init__(self):
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=lambda *args, **kwargs: None))
