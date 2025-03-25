#codebase 

## My request
Please don't create any files that will be created automatically by command. First we run the commands then we handle edits. Also please provide instructions in step-by-step, and I will ask for the next step once done, in order to be able to address any errors or issues.

Need your assistance on how to:

- initiate git to push to: https://github.com/RASBR/dj_template.git and do the initial push called 'template files only'. Then prepare the .gitignore file.

- 

- start a django project called 'core'

At this stage, I don't want any login just a public landing page with two links one to the index.html page of the app 'website' and the other link to the index.html page in the app documentation

- start an app called 'website'
   * static files already in the main project folder in folder named ./static/assets
   * the templates html files to be used are stored in the main project folder under ./templates/admin folder
   * 

- start an app called 'documentation'
   * static files already in the main project folder in folder named ./static/assets
   * the templates html files to be used are stored in the main project folder under ./templates/documents folder

---

## 1 Git

After setting your git repository on the website i.e. [github](https://github.com/), copy its `link` and follow the below steps.

Step 1 - Initialize Git and create .gitignore:
```bash
# Initialize git repository
git init
```
```bash
# Create file .gitignore the content is found below
touch .gitignore
```
```bash
# Add remote repository
git remote add origin your_repository_link
```

### .gitignore
Create a new .gitignore file with common Django ignores:

````text
# Python
*.pyc
__pycache__/
*.py[cod]
*$py.class

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment variables
.env
````

After creating these files, run:
```bash
# Add all files
git add .
```
```bash
# Initial commit
git commit -m "template files only"
```
```bash
# Push to main branch
git push -u origin main
```

## 2 Virtual Environment (venv)
Let's create the virtual environment and Django project. I'll guide you through the steps:

Step 1 - Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv
```
```bash
# Activate virtual environment (Windows)
venv\Scripts\activate
```
```bash
# Install Django
pip install django
```
```bash
# Upgrade pip
python.exe -m pip install --upgrade pip
```

Step 2 - Create Django project 'core':
```bash
# Create Django project
django-admin startproject core .
```

## Set up the Python interpreter
To set up the Python interpreter to use the one inside your virtual environment in VS Code, follow these steps:

1. Open VS Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette
3. Type "Python: Select Interpreter" and select that command
4. A list of available Python interpreters will appear. Look for the one located in your virtual environment's directory (it should have "venv" in the path)
5. Click on that interpreter to select it

Alternatively, you can also:

1. Open VS Code settings (File > Preferences > Settings or `Ctrl+,`)
2. Search for "python.defaultInterpreterPath"
3. Update the path to point to your virtual environment's Python executable:
   - Windows: `d:\Django\titapa-sbr\venv\Scripts\python.exe`
   - Linux/Mac: `d:\Django\titapa-sbr\venv\bin\python`

Once you've selected the interpreter, new terminal windows in VS Code will automatically activate the virtual environment.




After running these commands, I'll help you modify the core settings and create the necessary apps. Let me know when you've completed these steps and we'll proceed with the next phase.

Note: The period (.) at the end of the django-admin command is important - it creates the project in the current directory rather than creating a new subdirectory.