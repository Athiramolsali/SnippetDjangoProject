# SnippetDjangoProject

A backend API for managing short notes (snippets) with tagging functionality. Built using Django Rest Framework (DRF), this app allows users to create, update, view, and delete snippets, as well as manage tags. It uses JWT for authentication.

---

## Features

- **Authentication APIs**:
  - Login API
  - Refresh Token API

- **CRUD APIs**:
  - Create, Read, Update, and Delete snippets.
  - Link snippets with tags, avoiding duplicate tags.

- **Tag Management**:
  - List all tags.
  - View snippets associated with a specific tag.

---

## Technologies Used

- Python
- Django
- Django Rest Framework (DRF)
- dbsqlite (or your database of choice)
- JWT Authentication

---

## Installation

### Prerequisites
- Python 3.10
- pip (Python package manager)
- SQLite

  
#### Python And Django Setup
Required Python Version: Python 3.10.X

1. Install required python packages  
    `pip install -r requirements.txt`
2. Create database migrations in django  
    `python manage.py makemigrations `
3. Write migration changes in database  
    `python manage.py migrate `        
4.  Create superuser  
    `python manage.py createsuperuser `
5.  Run Django server  
    `python manage.py runserver 0.0.0.0:8000 `



## Misc Python Notes
### How to run scripts with Django shell
1. Starting Django shell  
    `python manage.py shell 
2. Run an external script in the shell  
    `exec(open('scripts/filename.py').read())`
## How to delete all django database migration files
`find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`  
`find . -path "*/migrations/*.pyc"  -delete`

