# django_fresh

Step 1: Set up a Python virtual environment and install Django

Open your terminal
Navigate to your project directory (d:\Django\django_fresh)
Run these commands:

```cmd
python -m venv venv
venv\Scripts\activate  # On Windows
pip install django
```

After running these commands, you'll have a virtual environment with Django installed. The directory structure will look like:

```text
django_fresh/
├── venv/
└── ...other files
```

Step 2: Create a new Django project

Run this command in your terminal (make sure your virtual environment is activated):

```cmd
django-admin startproject config .
```

```text
django_fresh/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── venv/
└── ...other files
```

---

Creating a superuser in Django doesn't require django-allauth. The superuser functionality is built into Django's authentication system.

To create a superuser, first make sure your database is set up by running migrations, then create the superuser:

1. Run migrations first:

```bash
python manage.py migrate
```

2. Then create a superuser:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:

- Username
- Email address (optional)
- Password (it won't be visible as you type)
- Password confirmation

3. Run the server

```cmd
python manage.py runserver
```

After completing these steps, you'll have a superuser account that can access the Django admin interface at http://localhost:8000/admin/

Copy template original files to folder admiro/
Add the below to .gitignore

```markdown
# My template original files

admiro/
```
