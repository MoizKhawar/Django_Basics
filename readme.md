# Getting Started With Django
**This is a step-by-step guide to get started with Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.**

# CONTENTS
[1.Make virtual environment](#1make-virtual-environment)  
[2.Install django](#2install-django)  
[3.Create django project](#3create-django-project)  
[4.Run server](#4run-server)  
[5.Create 3 folders inside klazoo directory](#5create-3-folders-inside-klazoo-directory)  
[6.Make views.py file inside klazoo/klazoo directory](#6make-viewspy-file-inside-klazooklazoo-directory)  
[7.Now in Urls.py configuration add these lines](#7now-in-urlspy-configuration-add-these-lines)  
[8.Now in views.py file define home function](#8now-in-viewspy-file-define-home-function)\
[9. Now create home.html file inside templates folder](#9-now-create-homehtml-file-inside-templates-folder)  
[10. Now in settings.py file make this change](#10-now-in-settingspy-file-make-this-change)  
[11. Now run the server again](#11-now-run-the-server-again)



## 1.Make virtual environment
```bash
python -m venv .venv
source .venv\Scripts\activate # On Windows
```
```bash
python -m venv .venv
source .venv/bin/activate # On Unix or MacOS
```



## 2.Install django
```bash
pip install django
```



## 3.Create django project
```bash
django-admin startproject klazoo # to create in new directory
cd klazoo
```
```bash
django-admin startproject klazoo . # to create in current directory
```



## 4.Run server
```bash
python manage.py runserver # to check if everything is working
```



## 5.Create 3 folders inside klazoo directory
```bash
mkdir media
mkdir templates
mkdir static
```



## 6.Make views.py file inside klazoo/klazoo directory
```bash
cd klazoo
touch views.py
```



## 7.Now in Urls.py configuration add these lines
#### Just above `urlpatterns` list
```python
from . import views # Import the views module we made views.py
```
#### Inside `urlpatterns` list
```python
path('home/',views.home) # Add this line to map URL to home function in views.py
```



## 8.Now in views.py file define home function
#### This if want to add text/code directly in views.py
```python
from django.http import HttpResponse                      
def home(request):                                        
    return HttpResponse("Welcome to the Home Page") 
```
#### This if want to add html file in templates folder
```python
from django.shortcuts import render                      
def home(request):
    return render(request, 'home.html')
```



## 9. Now create home.html file inside templates folder
#### Add this demo code in home.html to check if everything is working
```html
<!DOCTYPE html>
<html lang="en"> 
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to the Home Page!</h1>
</body>
</html>
```
#### Now add this as we are now using html file from templates folder [Refer to step 8 second code block above](#this-if-want-to-add-html-file-in-templates-folder)


## 10. Now in settings.py file make this change
- scroll and find `TEMPLATES` list
- inside that find `'DIRS': [],`
- change it to `'DIRS': ["templates"],`



## 11. Now run the server again
#### To check if everything is working
```bash
python manage.py runserver
```
#### Now make html file changes in home.html as per your need and refresh the browser to see the changes.

## Congratulations! You have successfully set up a basic Django project and created a home page. You can now start building your web application further!
