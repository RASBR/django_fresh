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
