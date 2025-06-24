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

SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "your-secret-key"  
```

4. Run Migrations & Seed
```bash

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```
4.Authentication Flow
User registers via /register

Logs in via /login and receives a JWT token

Token is required in the Authorization header for protected routes:

```bash

Authorization: Bearer <access_token>
```
5.Authentication Flow
User registers via /register

Logs in via /login and receives a JWT token

Token is required in the Authorization header for protected routes:

```bash
Authorization: Bearer <access_token>
```

🚀 API Endpoints
```bash
Method	Route	        Auth?	Description
POST	 /register	    ❌	Register a new user
POST	 /login 	    ❌	Log in and get JWT token
GET	    /episodes	    ❌	Get all episodes
GET 	/episodes/<id>	❌	Get a single episode + guests
DELETE	/episodes/<id>	✅	Delete episode and appearances
GET	    /guests     	❌	Get all guests
POST	/appearances	✅	Add a guest appearance

```
6.Postman Testing
✅ Steps
-Open Postman

-Import challenge-4-lateshow.postman_collection.json

-Create and activate an environment:

-base_url: http://localhost:5000

-jwt: (leave blank)

-Use the collection to:

-Register

-Log in (automatically saves JWT to jwt variable)

-Test protected routes (POST /appearances, DELETE /episodes/<id>)

Models
User
```bash
Field	        Type	    Notes
id	            Integer	    PK
username	    String	    Unique, required
password_hash   String	    Hashed password
```

Guest
```bash
Field	    Type	    Notes
id	        Integer	    PK
name	    String	    Required
occupation	String	    Required
```

Episode
```bash
Field	Type	    Notes
id	    Integer	    PK
date	Date	    Required
number	Integer	    Required
                    Cascade delete appearances
```
Appearance
```bash
Field	    Type	    Notes
id	        Integer 	PK
rating	    Integer 	1-5 validation
guest_id	Integer	    FK to Guest, required
episode_id	Integer	    FK to Episode, required
```bash

✅ Submission Checklist

 PostgreSQL used (✅ no SQLite)

 Models with validations

 MVC architecture

 JWT auth on protected routes

 Seed data functional

 All routes tested in Postman

 Clean, complete README.md

 GitHub repo pushed

 GitHub Repository
 https://github.com/mercycheps/late-show-api-challenge?search=1


