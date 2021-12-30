# url - shortener

## How to run
### Setup your environment
```
python3 -m venv env
source env/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Migrate database and run server
```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Using the shortener

### url - shortener
Use the text input to put the long url. The shorten url will be displayed on the list.
