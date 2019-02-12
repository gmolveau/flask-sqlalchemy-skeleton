# Flask + SQLAlchemy + Unit tests

A skeleton/bootstrap of a Flask app with SQLAlchemy and unit tests.


### Get started

* Clone the project

```bash
$ git clone https://github.com/gmolveau/flask-sqlalchemy-skeleton
$ cd flask-sqlalchemy-skeleton
```

* Install dependencies

```bash
$ virtualenv venv -p python3
$ source venv/bin/activate
(venv) $ pip install -r requirements
```

* Create the database

```bash
(venv) $ flask reset-db
```

* Run the unit tests

```bash
(venv) $ python3 -m pytest tests/
```

* Run the server

```bash
(venv) $ flask run
```

* Open your browser on `localhost:5000`
