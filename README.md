# WolfandBadger test:

[![Test status](https://github.com/PHPMailer/PHPMailer/workflows/Tests/badge.svg)](https://github.com/bishopgabriel/wolfandbadger/actions)

### Create a simple CRUD app that requires Github Authentication

<p><strong style="color:orange">NOTE:</strong> This project was built in a simple approach. If more time is given, I could build a separate front-end (using ReactJS or VueJS) and connect it to the server. The server will be built as an API using rest_framework (which I already started on the "api" folder). Also, rather than running all the commands below, I could write a docker file to easily start the project in an isolated linux container with all the required dependencies.</p>
<p>Finally, sqlite was used to make the database easier to test the project. A live production will entail either of MySQL, MSSQL, or Postgres...and the changes can be made in the settings.py of the project to connect to the right database.</p>


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

- step 5: to run a test, run this command
```cmd
python manage.py test
```

- step 6: start the server by running this command
```cmd
python manage.py runserver
```