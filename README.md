# REST-API-Using-Django
# iSubmit Implementation Steps
## Prerequisites

### Before getting started with iSubmit, ensure that you have the following software installed on your system:

- Visual Studio or PyCharm
- Python (latest version)

# Installation

## To install iSubmit, follow these steps:

### Create a virtual environment using the following command:

```bash
python -m venv venv
```
Activate the virtual environment using this command:

```bash
venv\scripts\activate
```
Install Django framework:

```bash
python -m pip install django
```

Install Django REST framework:

```bash
pip install djangorestframework
```

## Database Migration

### To create the required database for iSubmit, execute the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running iSubmit

To run iSubmit on your local machine, execute the following command:

```bash
python manage.py runserver
```

### You should see a message like this:


Starting development server at http://127.0.0.1:8000/

## Admin Credentials

### To create a new admin user, execute the following command and provide the required details:

```bash
python manage.py createsuperuser
```

### You can use the following admin credentials to access the 

## admin dashboard:

Admin ID: admin

Password: admin1234

## Faculty Credentials

### You can use the following faculty credentials to login:

Email: test@gmail.com

Password: 12345


# That's it! You're ready to use iSubmit....!!!!
