github-statistics
=================
Show statistics information from Github

## Requirements
- Python 2.7 or higher
- django 1.10.0
- requests package
- sqlite3

## Deploy for dev

### Clone repo
```bash
$ git clone https://github.com/lalviarez/github-statistics.git
```

### Create virtualenv
```bash
$ cd github-statistics
$ python -m virtualenv venv
```

Now activate virtualenv workspace.

```bash
$ source ./venv/bin/activate 
```

### Upgrade pip
```bash
$ pip install --upgrade pip
```

### Install django
```bash
$ pip install django~=1.10.0
```

### Install requests package
```bash
$ pip install requests
```

### Run migrations
```bash
$ python manage.py migrate
```

### Run server
```bash
$ python manage.py runserver
```

In your browser go to url http://localhost:8000

... and have fun!

