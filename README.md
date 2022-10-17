## CXDojo Test Task

Web-application for displaying information about users and adding information from test files

___
### RUN

1. Crete virtual enviroment:

_run_  python -m venv .venv

2. Activate virtual environment:

_run_  source .venv/bin/activate (on Linux and macOS) or .venv\Scripts\activate (on Windows)

3. Install required libraries from file requirements.txt:

_run_  pip install -r requirements.txt

4. Make migrations:

_run_  python manage.py makemigrations

5. Run the migration:

_run_  python manage.py migrate

6. Сreate a user (email can be omitted):

_run_  python manage.py createsuperuser

7. Run server:

_run_  python manage.py runserver

8. Follow the link to the development server and log in