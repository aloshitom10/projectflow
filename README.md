# ProjectFlow

ProjectFlow is a lightweight, self-hosted project management web application built with Python and Django. It provides simple CRUD for Projects and Tasks, per-user ownership, and an easy-to-read dashboard. This repository contains the source code and templates for a beginner-to-intermediate Django full-stack project that uses plain HTML and CSS (no Bootstrap) and a SQL database (PostgreSQL recommended).

## Key Features

- Secure user registration and login (Django auth)
- Create / read / update / delete Projects and Tasks
- Task status, priority, and due dates
- Dashboard with statistics and progress indicators
- Owner-based data isolation (users only see their own data)
- Plain HTML5 templates and hand-written CSS (no Bootstrap)

## Tech Stack

- Python 3.14+
- Django (6.x compatible)
- PostgreSQL (recommended) or other SQL DB supported by Django
- HTML5 and CSS (no Bootstrap)

> Note: This project was intentionally configured to avoid SQLite and Bootstrap. The default database configuration in `projectflow/settings.py` uses environment variables and defaults to PostgreSQL.

## Repository layout

- `projectflow/` — Django project settings and global files
- `projectflow_app/` — main application: models, views, templates, static
- `projectflow_app/templates/` — all HTML5 templates
- `projectflow_app/static/style.css` — main site CSS

## Before you start

This README assumes you will run the project locally and push the repository to GitHub manually (you asked not to push automatically).

### 1) Prepare a virtual environment

```bash
# Windows (PowerShell)
python -m venv myenv
.\myenv\Scripts\Activate.ps1

# Windows (cmd)
python -m venv myenv
myenv\Scripts\activate.bat

# macOS / Linux
python3 -m venv myenv
source myenv/bin/activate
```

### 2) Install dependencies

There is no requirements.txt in the repo. Install the minimal dependencies below (or create a `requirements.txt` and add the packages):

```bash
pip install --upgrade pip
pip install django
# Recommended PostgreSQL driver (psycopg v3) with binary wheels
pip install "psycopg[binary]"
# Or, if you prefer psycopg2 binary (older driver):
# pip install psycopg2-binary
```

If you prefer, create a `requirements.txt` with:

```
django
psycopg[binary]
```

and then run `pip install -r requirements.txt`.

### 3) Configure environment variables

The project reads DB settings from environment variables in `projectflow/settings.py`. Set these before running migrations in your shell or create a `.env` and load it (or use a tool like `direnv` or `django-environ`):

Example (PowerShell):

```powershell
$env:DB_ENGINE='django.db.backends.postgresql'
$env:DB_NAME='projectflow'
$env:DB_USER='postgres'
$env:DB_PASSWORD='yourpassword'
$env:DB_HOST='localhost'
$env:DB_PORT='5432'
$env:DJANGO_SECRET_KEY='replace-this-with-a-secret'
$env:DJANGO_DEBUG='True'
```

Notes:
- If you do not have PostgreSQL available, you can install it locally or use a hosted DB service.
- For development only, you may temporarily set `DB_ENGINE` to `django.db.backends.sqlite3` and configure `NAME` to a path. This project was requested to avoid SQLite, so prefer PostgreSQL for parity with production.

### 4) Run migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5) Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Static files

Static files (CSS) are in `projectflow_app/static/style.css`. During development the Django dev server serves static files automatically when `DEBUG = True`. For production, run `collectstatic` and configure your web server.

```bash
python manage.py collectstatic
```

## CSS and Templates

All templates are HTML5 and use semantic elements and ARIA attributes. The project intentionally uses hand-authored CSS (`style.css`) located under `projectflow_app/static/` so there is no dependency on Bootstrap.

## Git and GitHub

Suggested `.gitignore` entries (create a `.gitignore` in the repo root):

```
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual env
myenv/
.env
venv/

# Django
*.sqlite3
staticfiles/
media/

# IDEs
.vscode/
.idea/

# Byte-compiled
*.pyc
```

When you're ready to push:

```bash
git init
git add .
git commit -m "Initial commit - ProjectFlow"
# create remote and push
git remote add origin <your-repo-url>
git push -u origin main
```

## Troubleshooting

- If you see errors about `psycopg` / `psycopg2` missing, install `psycopg[binary]` or `psycopg2-binary` in the same virtual environment used to run `manage.py`.
- If templates or CSS don't update, make sure the dev server is running and `DEBUG = True`.
- If you changed the DB settings, re-run `migrate` after updating environment variables.

## Next steps (optional)

- Add a `requirements.txt` for reproducible installs: `pip freeze > requirements.txt` after installing packages.
- Add tests and a CI workflow (GitHub Actions) to run migrations and tests on push.
- Add Dockerfile and docker-compose for local DB and app orchestration.

## License

This project does not include a license file by default. Add one (for example MIT) if you plan to make the repository public.

---

If you want, I can also generate a `requirements.txt` and a `.gitignore` file now. Let me know which DB driver you prefer (`psycopg[binary]` or `psycopg2-binary`) and I will add a `requirements.txt` accordingly.