# WolfandBadger
Wolf and Wadger test:

### Create a simple CRUD app that requires Github Authentication

## How to setup and run project locally on your device

- step 1: clone the repository, then create a virtual environment by running the following commands

```cmd
pip install virtualenv
```
```cmd
virtualenv venv
```
```cmd
venv\Scripts\activate
```

- step 2: install the dependencies

```cmd
pip install -r requirements.txt
```

- step 3 (optional): the migrations has already been setup, but you can re-run again by running these commands
```cmd
python manage.py makemigrations
```
```cmd
python manage.py migrate
```

- step 4: Enter your github app credentials (client_id and secret) in the wolfandbadger/settings.py of the project (lines 96 and 97)
```python
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
```

- step 5: start the server by running this command
```cmd
python manage.py runserver
```