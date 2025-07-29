class OpenAI:
    def __init__(self):
        self.chat = self.Chat()

    class Chat:
        def __init__(self):
            self.completions = self.Completions()

        class Completions:
            def create(self, *args, **kwargs):
                raise NotImplementedError("OpenAI API not available in this environment")

from . import types

__all__ = ["OpenAI", "types"]
