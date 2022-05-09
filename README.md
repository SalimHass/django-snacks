# Django 
in this lab we started working with django, here is the steps we followed to creat the project and its app:

1. create a poetry new project and give it the desired name
2. poetry install 
3. poetry shell
4. poetry add django 
5. remove the porject and the test folders
6. use `django-admin startproject project_name`
7. use `python manage.py migrate` to set the database
8. use `python manage.py createsuperuser` to assign superuser
9. use `python manage.py runserver` to check everything is ok and the server works fine
10. inside the project folder use `python manage.py startapp app_name` to make a new app
11. inside the settings.py of the project add the app name to the installed_apps list
12. add models to the models.py in the app
13. create views -using templates- inside the views.py of the app
14. add urls.py in the app folder and add to it the desired paths
15. add the app urls.py to the projects urls.py , using include and import include in the top
16. add `os.path.join(BASE_DIR, 'templates')` to the settings.py under TEMPLATES-> "DIRS" list
17. after each adding to a model use `python manage.py makemigrations` and then `python manage.py migrate`
-----
## in this lab
we created only two paths , Home and About . with template that states where are we when called.
