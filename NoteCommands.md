# Commands
	

---
## pip3 install *packages
- => pip3 install django
- => pip3 install djangorestframework
- => pip3 install django_elasticsearch_dsl
- => pip3 install django_elasticsearch_dsl_drf
- => pip3 install requests


## install packages
- => cd projdemo
- => pip3 freeze > requirements.txt
- install package dependency
- => pip3 install -r requirements.txt


---
- check django version
- => django-admin --version


---
- make project
- => django-admin startproject projdemo

---
- make app
- => python3 manage.py startapp login


---
- => python3 manage.py makemigrations
- => python3 manage.py migrate


---
- create super user
- => python3 manage.py createsuperuser