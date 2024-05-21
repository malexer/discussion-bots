from discussion_bots import config
from discussion_bots.bot import Bot
from discussion_bots.chat import OpenAiChat


def main():
    chat = OpenAiChat(model=config.MODEL)
    bots = [Bot(name) for name in ["Optimus", "T-800", "WALL-E"]]

    print("Starting chat session.")
    chat.create_session(bots)

    for _ in range(4):
        for bot in bots:
            print(f" - {bot.name} is talking...")
            chat.ask(bot)

    print("\nChat history:")

    for message in chat.dump_messages():
        print(f"\n{message}")


if __name__ == "__main__":
    main()
