from enum import Enum


class PostTodoUpdateProduct(str, Enum):
    CHALLENGE = "challenge"
    MACHINE = "machine"
    SHERLOCK = "sherlock"

    def __str__(self) -> str:
        return str(self.value)
