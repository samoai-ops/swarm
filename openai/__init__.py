class OpenAI:
    def __init__(self, *args, **kwargs):
        from types import SimpleNamespace
        self.chat = SimpleNamespace()
        self.chat.completions = SimpleNamespace(create=self._not_implemented)

    def _not_implemented(self, *args, **kwargs):
        raise NotImplementedError("OpenAI stub cannot make API calls")
