# todoAPI
ToDo app created with Backend on Django and Frontend on React

## Getting started:

### Create and activate virtualenv
```commandline
virtualenv .venv -p python3
. .venv/bin/activate
```

### Install requirements
```commandline
pip install Poetry
poetry install
```

### Activate pre-commit configuration
```commandline
pre-commit install
```

### Migrate database
```commandline
cd backend
python manage.py migrate
```

### Run server

#### Run Backend
```commandline
cd backend
python manage.py runserver
```
