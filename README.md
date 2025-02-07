<h1>Backend Code For Feedback Form</h1>

Create venv using
### `python -m venv nameofvenv`

Activate venv
### `venv\Scripts\activate.bat`

Install django using
### `pip install django`

Start a new django project using
### `django-admin startproject projectname`

Install packages for restframwork
### 
     pip install djangorestframework
	   pip install pillow
	   pip install django-cors-headers

Start a app using
### `python manage.py startapp appname`

Run your server using
### `python manage.py runserver`

Include your appname in INSTALLED_APPS
###
    add 'rest_framework.authtoken' in INSTALLED_APPS for token verification
	  add 
		REST_FRAMEWORK = {
    			'DEFAULT_AUTHENTICATION_CLASSES': [
			'rest_framework.authentication.TokenAuthentication',
			],
    			'DEFAULT_PERMISSION_CLASSES': [
			'rest_framework.permissions.IsAuthenticated',
			],
		}
		this part in settings.py
  
set STATIC_URL , STATIC_ROOT , MEDIA_URL , MEDIA_ROOT
in root urls.py set MEDIA_URL and document_root=MEDIA_ROOT inside static



In the project directory, you can run:
### `npm start`
