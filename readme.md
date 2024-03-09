YouTube Demo: https://youtu.be/DBUyBhcQ1Ww
Github: https://github.com/hannalam/YogaCollabHub
AWS: http://13.48.127.8:8000/


# List of development environment:

operating system: Window 11
python version: Python 3.11.8

# How to run this web

python -m pip install virtualwrapper
py -3 -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
python manage.py runserver 127.0.0.1:8080

# Logging into django-admin:super user

username: user
password: user1234

# Location of the data loading script

yogacollabhub/db.sqlite3

# How to run the unit test:

python manage.py test
python manage.py test users.tests
python manage.py test session.tests
python manage.py test interactions.tests
python manage.py test enrollments.tests


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

Enter the directory

`cd YogaCollabHub`

Reload the update on AWS

`git pull origin main`

- This is the public ip for this project: http://13.48.127.8:8000/
