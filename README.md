# Install dependences
The only thing that you need is Django. It was coded in Django 1.9.

	pip install django

# Running
To run the server you just need to apply migrations to de database and runserver. By default it's using SQLite3.

	python3 manage.py migrate
  python3 manage.py runserver

And it should be running on http://localhost:8000
