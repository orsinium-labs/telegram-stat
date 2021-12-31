from itertools import chain
import telethon
from telethon.tl.patched import Message
from typing import Any, Dict, Iterator, NamedTuple, Tuple


class Channel(NamedTuple):
    name: str
    client: telethon.TelegramClient

    @property
    def posts(self) -> Iterator["Post"]:
        for message in self.client.iter_messages(self.name):
            yield Post(message)


class Post(NamedTuple):
    message: Message

    @property
    def buttons(self) -> Iterator[Tuple[str, int]]:
        buttons = self.message.buttons
        if not buttons:
            return
        for button in chain(*buttons):
            reaction, _, count = button.button.text.partition(' ')
            if count.isdigit():
                yield reaction, int(count)
            else:
                yield button.button.text, 0

    def as_dict(self) -> Dict[str, Any]:
        m = self.message
        return dict(
            id=m.id,
            date=m.date.isoformat(),
            text=m.message,
            views=m.views or 0,
            forwards=m.forwards or 0,
            buttons=dict(self.buttons),
        )
