from typing import Generator
from uuid import UUID, uuid4


def create_random_uuid() -> Generator:
    data = set()

    while True:
        new_value: UUID = uuid4()

        if new_value in data:
            continue
        else:
            data.add(new_value)

        yield new_value


class User:
    random_uuid: Generator = create_random_uuid()

    def __init__(self, username: str) -> None:
        self.id_: UUID = next(self.random_uuid)
        # self.id_: UUID = create_random_uuid()
        self.username: str = username

    def __str__(self) -> str:
        return f"{self.username=}, {self.id_}"


john = User(username="John")
another_john = User(username="John")
marry = User(username="Marry")

print(john)
print(another_john)
print(marry)
