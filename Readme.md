# worldclass.ro scraper for classes

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
