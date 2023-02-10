##about requirements.txt
	pip freeze > requirements.txt
	pip install -r requirements.txt

###Python env

#install
pip install virtualenvwrapper-win

#criar
mkvirtualenv myapp

#ativar env
workon myapp 

#desativa env
deactivate


###Django

#install
	pip install django
	
#criar projeto	
	django-admin startproject myproject
	
#criar o app	
	python manage.py startapp myappa	

#rodar o app
	python manage.py runserver

# make miogration
	python manage.py makemigrations



#To use postgres, intall:
	pip install psycopg2		
	pip install Pillow

# atualizar o pip
	python.exe -m pip install --upgrade pip	