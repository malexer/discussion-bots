# discussion-bots

Experimenting with the OpenAI API for Multi-Bot Discussions.


## Description

This repository contains a Python application that simulates a chat
between multiple bots using OpenAI's GPT models. The bots take turns
to talk in a chat session.

Check the prompt in the `discussion_bots.prompt` module.


## Usage

To run the application, do the following:

1. Define required environment variables. e.g. by setting them in a `.env` file:

```shell
OPENAI_API_KEY=<value>
OPENAI_ORG_ID=<value>
OPENAI_PROJECT_ID=<value>
```

2. Create and activate virtual environment.
3. Install the dependencies: `poetry install`
4. Run the application: `poetry run python main.py`


## Requirements

- Python 3.12
- poetry
