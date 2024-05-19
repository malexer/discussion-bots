from enum import Enum


class Model(str, Enum):
    GPT_35_turbo = "gpt-3.5-turbo"
    GPT_4o = "gpt-4o"


MODEL = Model.GPT_4o
