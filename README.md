#  Late Show API Challenge

A Flask-based REST API for managing a Late Night Show guest system, using PostgreSQL and JWT token authentication.

---

# Project Structure


.
├── challenge-4-lateshow.postman_collection.json
├── LICENSE
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 30d8c88fe9e0_add_models.py
├── README.md
└── server
    ├── __pycache__
    │   ├── app.cpython-38.pyc
    │   ├── config.cpython-38.pyc
    │   └── extensions.cpython-38.pyc
    ├── app.py
    ├── config.py
    ├── controllers
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── appearance_controller.cpython-38.pyc
    │   │   ├── auth_controller.cpython-38.pyc
    │   │   ├── episode_controller.cpython-38.pyc
    │   │   └── guest_controller.cpython-38.pyc
    │   ├── appearance_controller.py
    │   ├── auth_controller.py
    │   ├── episode_controller.py
    │   └── guest_controller.py
    ├── extensions.py
    ├── models
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── appearance.cpython-38.pyc
    │   │   ├── episode.cpython-38.pyc
    │   │   ├── guest.cpython-38.pyc
    │   │   └── user.cpython-38.pyc
    │   ├── appearance.py
    │   ├── episode.py
    │   ├── guest.py
    │   └── user.py
    ├── seed.py
    └── testing
        ├── conftest.py
        └── test_routes.py


---

# Setup Instructions

 1.Install Dependencies

Make sure you have **Python 3.8+**, **PostgreSQL**, and **Pipenv** installed.

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```
2. Create PostgreSQL Database
```bash
CREATE DATABASE late_show_db;
```

3. Configure server/config.py

```bash
python
Copy code
SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "your-secret-key"  
```

4. Run Migrations & Seed
```bash
Copy code
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

