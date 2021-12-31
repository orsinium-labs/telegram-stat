# telegram-stat

A CLI tool to extract [Telegram](https://telegram.org/) channel statistics as [ndJSON](http://ndjson.org/).

## Installation

```bash
git clone https://github.com/orsinium-labs/telegram-stat.git
cd telegram-stat
python3 -m pip install -r requirements.txt
```

## Usage

To get access to telegram API, you'll need `api_id` and `api_hash` that you can obtain at [my.telegram.org](https://my.telegram.org/apps).

Get statistics for [@pythonetc](https://t.me/s/pythonetc):

```bash
python3 -m telegram_stat \
    --channel pythonetc \
    --api-id 12345
    --api-hash 1234567890abcdef \
    > pythonetc.ndjson
```

See [top_posts.ipynb](./top_posts.ipynb) for an example on how to analyze the resulting data using [pandas](https://pandas.pydata.org/).
