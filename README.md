# Welcome To Checkers Board Game - made in Django framework

### gameplay:
<img style="-webkit-user-select: none;margin: auto; " src="https://raw.githubusercontent.com/zealpatel1990/CheckersBoard-Django/zeal_branch/screenshots/Screen%20Shot%202020-12-11%20at%203.00.55%20PM.png" width="783" height="373">

### game sessions:
<img style="-webkit-user-select: none;margin: auto;" src="https://raw.githubusercontent.com/zealpatel1990/CheckersBoard-Django/zeal_branch/screenshots/Screen%20Shot%202020-12-11%20at%202.59.56%20PM.png" width="783" height="373">

### game recording:
<img style="-webkit-user-select: none;margin: auto;" src="https://raw.githubusercontent.com/zealpatel1990/CheckersBoard-Django/zeal_branch/screenshots/Screen%20Shot%202020-12-11%20at%203.01.18%20PM.png" width="383" height="373">


# Installation Instruction
My system windows10, python3.8.6, django3.1.1

First download project: `git clone https://github.com/zealpatel1990/CheckersBoard-Django.git`

Django project is in 'mysite' folder, s change directory: `cd CheckersBoard-Django/mysite`

To install requirements/supporting library: `pip install requirements.txt`

Also Install Docker and run it: https://docs.docker.com/get-docker/

We are using MySQL, (you can change it) so intall it and set root user password root. Also start server.

Before running project Make sure to turn on Docker, Mysql server with username: root and password: root (else change your mysite/mysite/settings.py)

Run `python manage.py makemigrations`
Run `python manage.py migrate`


Before running project Make sure to turn on Docker, Mysql server with username: root and password: root (else change your mysite/mysite/settings.py)
FINALLY To run project: `python manage.py runserver 0.0.0.0:8000`
<0.0.0.0 means all incoming requests will be accepted and :8000 is port of system which is running>

##Some extras

the design docs file contains some files that are built on 
draw.io to open these docs go to draw.io and load them to the site.

this project conisit of three main parts a mySQL DB a Flask bakc end and a vue front end 
style quides for each of these parts can be found below 

To start Redis manually use this commond: `docker run -p 6379:6379 -d redis:2.8`



