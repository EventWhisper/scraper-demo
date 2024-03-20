# demo scraper for eventwhisper

a simple demo scraper for eventwhisper. Scrapers are called by the whisper core. The scraper is responsible for fetching events from a source and returning them to the core. The core then processes and stores the events. Scrapers are expected to be stateless and idempotent. It only scrapes and returns the resulting events.

## quickstart

```bash
$ git clone git@github.com:EventWhisper/scraper-demo.git
$ cd scraper-demo
$ python -m venv .venv
$ pip install -r requirements.txt
$ env FLASK_APP=app/main.py APP_TOKEN=foobar DEBUG=True python -m flask run
```

## features

* three different routes
    * `/` - returns a simple hello world
    * `/events` - returns a list of events
    * `/metrics` - returns a list of prometheus metrics
* token based authentication
* prometheus metrics for the last scrape