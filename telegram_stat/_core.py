import telethon
from typing import Iterator, NamedTuple


class Channel(NamedTuple):
    name: str
    client: telethon.TelegramClient

    @property
    def posts(self) -> Iterator["Post"]:
        ...


class Post(NamedTuple):
    views: int
    text: str
    id: int
