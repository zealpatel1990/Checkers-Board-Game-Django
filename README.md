# Welcome To Checkers Board Game - made in Django framework

### gameplay:
![Screenshot (45)](https://user-images.githubusercontent.com/28397002/141667443-191d7adc-fa2e-4f74-aa03-99ca5f6f8a4d.png)

### game sessions:
![image](https://user-images.githubusercontent.com/28397002/141667863-1cef07fb-3433-4f8c-81bb-866d5a6f3d6a.png)

### game recording:
![image](https://user-images.githubusercontent.com/28397002/141667894-7fbb2046-cef8-4bc4-bc33-75e85c0e224b.png)


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



