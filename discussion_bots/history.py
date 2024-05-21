from dataclasses import dataclass

from pydantic import BaseModel


class Message(BaseModel):
    role: str

    content: str

    @classmethod
    def build_prompt(cls, content: str):
        return cls(role="system", content=content)

    @classmethod
    def build(cls, is_from_me: bool, content: str):
        """Build a message.

        Args:
            is_from_me: Whether the message is from the current bot.
            content: The content of the message.
        """
        return cls(
            role="assistant" if is_from_me else "user",
            content=content,
        )


@dataclass
class Reply:
    from_name: str
    content: str

    def __str__(self):
        return f"{self.from_name}: {self.content}"


class ChatHistory:
    def __init__(self):
        self._history: list[Reply] = []

    def __len__(self):
        return len(self._history)

    def add_reply(self, from_name: str, content: str):
        """Add a reply to the chat history.

        Args:
            from_name: The name of the bot who sent the message.
            content: The content of the message.
        """
        self._history.append(Reply(from_name, content))

    def serialize(self, for_name: str, prompt: str) -> list[dict]:
        """Serialize the prompt and chat history for a given bot.

        Args:
            for_name: The name of the bot to serialize the history for.
            prompt: The bot's prompt.
        """
        chat = [
            Message.build_prompt(prompt),
            *(
                Message.build(
                    is_from_me=reply.from_name == for_name,
                    content=str(reply),
                )
                for reply in self._history
            ),
        ]

        return [message.model_dump() for message in chat]

    def dump(self) -> list[Reply]:
        return self._history
