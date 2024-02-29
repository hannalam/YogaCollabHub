run later
py -m pip freeze > requirements.txt

# List of development environment:

operating system: Window 11
python version: Python 3.10.11

Logging into django-admin:

# super user

username: user
password: user1234

# How to run the unit test:

python manage.py test

# Location of the data loading script

yogacollabhub/db.sqlite3

# How to run this web

python -m pip install virtualwrapper
py -3 -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
python manage.py runserver 127.0.0.1:8080

# Reference of media used

learn from: How to Build a Web Assistant Using Django and ChatGPT API in Python  
https://thepythoncode.com/article/web-assistant-django-with-gpt3-api-python?utm_content=cmp-true

certificate
https://www.vinyasayogaashram.com/image/rys-200.jpg

# Steps To Deploy on Amazon EC2

Update the System

`sudo dnf update -y`

Install Git

`sudo dnf install git -y`

To get this repository, run the following command inside your git enabled terminal

`git clone https://github.com/hannalam/YogaCollabHub.git`

Install pip

`sudo dnf install pip -y`

Install Django

`pip install django`

Make Migrations

`python3 manage.py makemigrations`

Migrate

`python3 manage.py migrate`

Createsuperuser

`python3 manage.py createsuperuser`

Runserver

`python3 manage.py runserver 0.0.0.0:8000`
