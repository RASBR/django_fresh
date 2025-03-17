# django_fresh

Step 1: Set up a Python virtual environment and install Django

Open your terminal
Navigate to your project directory (d:\Django\django_fresh)
Run these commands:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install django
```

After running these commands, you'll have a virtual environment with Django installed. The directory structure will look like:

```bash
django_fresh/
├── venv/
└── ...other files
```

Step 2: Create a new Django project

Run this command in your terminal (make sure your virtual environment is activated):

```bash
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

```bash
python manage.py runserver
```

After completing these steps, you'll have a superuser account that can access the Django admin interface at http://localhost:8000/admin/

Copy template original files to folder admiro/
Add the below to .gitignore

```markdown
# My template original files

admiro/
```

Let me help structure this change. We need to update all SVG fragment identifiers in the static URLs.

Step-by-step:

1. Move the fragment identifier (#) outside of the static tag
2. Apply across all templates

### [user-profile.html](file:///d%3A/Django/django_fresh/templates/account/user-profile.html)

This is the main file that needs updates. Here's how to modify the SVG references:

```html
// ...existing code...
<use href="{% static 'assets/svg/iconly-sprite.svg' %}#Category"></use>
// ...existing code...
<use href="{% static 'assets/svg/iconly-sprite.svg' %}#Search"></use>
// ...existing code...
<use href="{% static 'assets/svg/iconly-sprite.svg' %}#moondark"></use>
// ...existing code...
```

To make icons work:
The pattern to follow is:

- Change: `href="{% static 'assets/svg/iconly-sprite.svg#Search' %}"`
- To: `href="{% static 'assets/svg/iconly-sprite.svg' %}#Search"`

Repeat this pattern for all SVG fragment identifiers in all your HTML templates. This change ensures better URL handling while maintaining the fragment identifier functionality.

Note: This change needs to be applied across all template files that use SVG sprites. Would you like me to show the changes for the other template files as well?

The pattern to follow is:

Change: href="{% static 'assets/svg/iconly-sprite.svg#Search' %}"
To: href="{% static 'assets/svg/iconly-sprite.svg' %}#Search"

"../assets/images/favicon.png" becomes "{% static 'assets/images/favicon.png' %}"
"../assets/js/vendors/bootstrap/dist/js/popper.min.js" becomes {% static 'assets/js/vendors/bootstrap/dist/js/popper.min.js' %}"
"../assets/css/bulk-style.css" becomes {% static 'assets/css/bulk-style.css' %}"

Made changes.
