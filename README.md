
# Django-Test-App
This is a little test using django
![Desktop](./screenshots/capture.png)

## How to start the project

+ To start the project create an environment (preferably)

	`Python -m venv venv`
	
+ And start it
	`source venv/bin/activate`

+ Install everything in requirements.txt
	
	`pip install requirements.txt`

+ Inside in the folder src create an .env that must contain:
SECRET_KEY and DEBUG_STATE

+ Do the migrations
`python manage.py makemigrations`
`python manage.py migrate`

+ And start
`python manage.py runserver`


+ If the database didn't work for some reason, try this:
`python manage.py migrate --run-syncdb`