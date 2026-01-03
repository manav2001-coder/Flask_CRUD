# Flask Authentication & Funds API

A modular Flask RESTful API with user signup/login, secure password hashing, and SQLAlchemy persistence. Built using the application factory pattern.

## Features
- Modular Blueprints for auth and core logic
- Secure password hashing (werkzeug)
- SQLAlchemy models for users and funds
- Simple JSON REST endpoints for signup/login

## Quickstart
1. Clone the repo:
   git clone <your-repo-url>
   cd my_project
2. Create and activate a virtualenv:
   python -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install flask flask-sqlalchemy PyJWT werkzeug pymysql
4. Configure database in [`Config`](config.py)
5. Run the app:
   python run.py

## Configuration
Edit the database URI in [`Config`](config.py).

## Key files & symbols
- App factory: [`create_app`](app/__init__.py) — [app/__init__.py](app/__init__.py)  
- Entry point: [run.py](run.py)  
- Auth blueprint: [`auth`](app/auth.py) — [app/auth.py](app/auth.py)  
- DB instance: [`db`](app/db.py) — [app/db.py](app/db.py)  
- Models: [`User`](app/models/__init__.py), [`Funds`](app/models/__init__.py) — [app/models/__init__.py](app/models/__init__.py)  
- Config class: [`Config`](config.py) — [config.py](config.py)

## API (examples)
- POST /signup/ — JSON { firstName, lastName, email, password } (creates a user)
- POST /login/ — JSON { email, password } (returns success/failed)

## Development
- App initializes DB via `db.create_all()` inside [`create_app`](app/__init__.py).
- Run with debug during development: python run.py

## Notes
- Ensure your DB URI in [`Config`](config.py) points to a reachable database.
- Add tests and environment-based config for production readiness.
