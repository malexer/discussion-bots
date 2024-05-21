from openai import OpenAI
from openai.types.chat import ChatCompletion

from discussion_bots.bot import Bot
from discussion_bots.history import ChatHistory


class OpenAiChat:
    """Client for OpenAI API.

    Note: variables OPENAI_API_KEY, OPENAI_ORG_ID, OPENAI_PROJECT_ID
    should be defined in your environment.
    """

    def __init__(self, model: str):
        self._model = model
        self._client = self._build_client()
        self._chat_history = ChatHistory()

    def _build_client(self) -> OpenAI:
        return OpenAI()

    @staticmethod
    def _extract_message(chat_completion: ChatCompletion) -> str:
        return chat_completion.choices[0].message.content

    def _ask_chat_gpt(self, previous_messages: list[dict]) -> str:
        chat_completion = self._client.chat.completions.create(
            model=self._model,
            messages=previous_messages,
        )
        return self._extract_message(chat_completion)

    def create_session(self, bots: list[Bot]):
        """Create a new chat session.

        Args:
            bots: A list of bots participating in the chat.
        """

        self._chat_history = ChatHistory()
        for n, bot in enumerate(bots):
            i_am_first = n == 0
            bot.initialize(i_am_first)

    def ask(self, bot: Bot):
        bot_response = self._ask_chat_gpt(
            previous_messages=self._chat_history.serialize(
                for_name=bot.name, prompt=bot.prompt
            ),
        )

        self._chat_history.add_reply(from_name=bot.name, content=bot_response)

    def dump_messages(self) -> list[str]:
        return [
            f"{reply.from_name}: {reply.content}" for reply in self._chat_history.dump()
        ]
