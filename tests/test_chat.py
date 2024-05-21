from unittest.mock import Mock

import pytest
from mockito.matchers import captor

from discussion_bots.bot import Bot
from discussion_bots.chat import OpenAiChat


@pytest.fixture
def mock_client(when):
    return when(OpenAiChat)._build_client().thenReturn(Mock())


def message_generator():
    n = 1
    while True:
        yield f"Message {n}"
        n += 1


def test_two_bots_can_chat(mock_client, expect, patch):
    mocked_messages = message_generator()
    arguments = captor()

    bots = (Bot("AI1"), Bot("AI2"))

    chat = OpenAiChat(model="BUDGET_MODEL")
    chat.create_session(bots)

    for _ in range(2):
        for bot in bots:
            expect(OpenAiChat)._ask_chat_gpt(previous_messages=arguments).thenReturn(
                next(mocked_messages)
            )

            chat.ask(bot)

    previous_messages_ai1_first = arguments.all_values[0]
    assert len(previous_messages_ai1_first) == 1
    assert previous_messages_ai1_first[0]["role"] == "system"
    assert 'Your name is "AI1"' in previous_messages_ai1_first[0]["content"]

    previous_messages_ai2_first = arguments.all_values[1]
    assert len(previous_messages_ai2_first) == 2
    assert previous_messages_ai2_first[0]["role"] == "system"
    assert 'Your name is "AI2"' in previous_messages_ai2_first[0]["content"]
    assert previous_messages_ai2_first[1] == {
        "role": "user",
        "content": "AI1: Message 1",
    }

    previous_messages_ai1_second = arguments.all_values[2]
    assert len(previous_messages_ai1_second) == 3
    assert previous_messages_ai1_second[0]["role"] == "system"
    assert 'Your name is "AI1"' in previous_messages_ai1_second[0]["content"]
    assert previous_messages_ai1_second[1] == {
        "role": "assistant",
        "content": "AI1: Message 1",
    }
    assert previous_messages_ai1_second[2] == {
        "role": "user",
        "content": "AI2: Message 2",
    }

    previous_messages_ai2_second = arguments.all_values[3]
    assert len(previous_messages_ai2_second) == 4
    assert previous_messages_ai2_second[0]["role"] == "system"
    assert 'Your name is "AI2"' in previous_messages_ai2_second[0]["content"]
    assert previous_messages_ai2_second[1] == {
        "role": "user",
        "content": "AI1: Message 1",
    }
    assert previous_messages_ai2_second[2] == {
        "role": "assistant",
        "content": "AI2: Message 2",
    }
    assert previous_messages_ai2_second[3] == {
        "role": "user",
        "content": "AI1: Message 3",
    }
