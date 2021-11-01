# boilerplate-django

Steps I took to building this boilerplate.

Django Startup

  1. mkdir <directory name>
  2. cd <directory name>
  3. pipenv shell
  4. python -m pip install Django
  5. django-admin startproject core
  6. python manage.py migrate
  
  
Next I use the startapp command to set up the basic part of the website. Im going to add in custom user accounts so I have started a app for that. Accounts will have the signup, login/logout functions and emailing functions for authenticating users.
  
  
start app
  1. python manage.py startapp home
  2. python manage.py startapp blog
  3. python manage.py startapp accounts
  
  
Update installed app in settings.py 

  
  # Handy commands
  
  Github quoting code in docs
  
  
  `cmd/ ctrl + e`
  
  
  Changing port
  
  `python manage.py runserver <port number>`
  
  Changing Ip and Port
  
  `python manage.py runserver <ip>:<port number> `
