# worldclass.ro scraper for classes

Scenario: you have a gym subscription at [World
Class](https://www.worldclass.ro/). You're interested in a handful of classes
in a handful of locations. The website makes you click through lots of pages to
scan the calendar so you can pick your classes. This tool filters the calendar
to what you care about so you can scan it easily.

## Development

```
python3 -m venv venv --upgrade-deps
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py wcls_sync
./manage.py runserver
```
