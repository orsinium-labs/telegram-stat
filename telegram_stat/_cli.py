from argparse import ArgumentParser
import json
import sys
import typing
import telethon
from ._core import Channel


def run(argv: typing.List[str], stream: typing.TextIO) -> int:
    parser = ArgumentParser()
    parser.add_argument("--channel", required=True)
    parser.add_argument("--api-id", required=True)
    parser.add_argument("--api-hash", required=True)
    args = parser.parse_args(argv)
    client = telethon.TelegramClient(
        session='telegram_stat',
        api_id=args.api_id,
        api_hash=args.api_hash,
    )
    client.start()
    channel = Channel(name=args.channel, client=client)
    for post in channel.posts:
        print(json.dumps(post.as_dict()))
    return 0


def entrypoint() -> typing.NoReturn:
    code = run(argv=sys.argv[1:], stream=sys.stdout)
    sys.exit(code)
