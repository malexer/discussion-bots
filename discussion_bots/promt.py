class Prompt:

    INTRO = "You are in a meeting with a group of software engineers."

    TASK = (
        "This group is discussing which language to choose for the "
        "scripts which you need to write for the project. "
        "These scripts will be used to automate the deployment. "
        "Currently you are using sh and bash scripts. But everybody "
        "aggrees that it is time to move to a more modern language."
    )

    TODO_FIRST = "Please, start the discussion."
    TODO_OTHERS = "Please, join the discussion."

    SPECS = (
        "I will post the answers from other team members. Each answer is "
        'in format "<name>: <answer>". Your name is "{name}". '
        "Please, provide your answer without name prefix. The format "
        'of your response should be "<answer>". '
        "Do not repeat the language that was already mentioned. "
        "We need to compare different alternatives. "
        "The discussion should end after 3 messages from each member. "
        "Limit each message to 2 sentences maximum. "
        "Do not write essays. Keep it short and to the point. "
        "But mention the pros and cons. "
        "In the end we should get a decision. "
        "Please, make sure that the decision is clear and one specific "
        "language is chosen. "
        "Do not repeat the decision multiple times. If you see that the "
        "decision is already made, you can end the discussion."
    )

    @classmethod
    def generate(cls, name: str, starting_discussion: bool = False):
        """Generate a prompt for the bot.

        Args:
            name: The name of the bot.
            starting_discussion: Whether the bot is the first one to post.
        """
        return "\n".join(
            [
                cls.INTRO,
                cls.TASK,
                cls.TODO_FIRST if starting_discussion else cls.TODO_OTHERS,
                cls.SPECS.format(name=name),
            ]
        )
