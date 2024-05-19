from discussion_bots.promt import Prompt


class Bot:
    def __init__(self, name: str):
        self.name = name
        self._prompt = None

    @property
    def prompt(self) -> str:
        if self._prompt is None:
            self.initialize()

        return self._prompt

    def initialize(self, i_should_start_discussion: bool = False):
        self._prompt = Prompt.generate(
            name=self.name,
            starting_discussion=i_should_start_discussion,
        )
