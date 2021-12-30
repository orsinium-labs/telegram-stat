import telethon
from telethon.tl.patched import Message
from typing import Any, Dict, Iterator, NamedTuple


class Channel(NamedTuple):
    name: str
    client: telethon.TelegramClient

    @property
    def posts(self) -> Iterator["Post"]:
        for message in self.client.iter_messages(self.name):
            yield Post(message)


class Post(NamedTuple):
    message: Message

    def as_dict(self) -> Dict[str, Any]:
        m = self.message
        return dict(
            id=m.id,
            date=m.date.isoformat(),
            text=m.message,
            views=m.views,
            forwards=m.forwards,
        )
