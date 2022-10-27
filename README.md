
# Crime Activity Reporting Portal

	Platform through which a person can give tip-off about any suspicious activity/ crime
    to the authorities.

# Description
    There are cases when people have either witnessed a crime, have a suspicion, or are 
    aware that crime is being planned, but hesitant come forward to report. Forcing people 
    to identify themselves as part of providing a tip-off might therefore lead to missing 
    out on a lot of useful information. Crime Activity Reporting Portal will be a platform 
    through which a person can give tip-off about any suspicious activity or crime in a secure
    and completely anonymous manner. The platform will allow people to give out the most 
    useful information in the shortest amount of time. 

## Contributions are always welcome! 🪄

This is how you can contribute
```
	1. Fork This Repository
	2. Using Git on your local machine, clone your fork using the URL you just copied: git clone URL_OF_FORK
	3. Navigate to Repo enter cd NAME_OF_REPOSITORY
	4. git remote add upstream URL_OF_PROJECT
	5. git remote -v
	6. git pull upstream master
	7. git checkout -b BRANCH_NAME
	8. Make Changes
	9. git add .
       10. git commit -m "commit message"
       11. git push -u origin BRANCH_NAME
```
Please adhere to this project's [Code Of Conduct](https://github.com/Kunalp02/Crime_Reporting_Portal/blob/master/CODE_OF_CONDUCT.md).


## Documentation

[Documentation](https://docs-six-gamma.vercel.app)


## Run Locally

Clone the project

```cmd
  git clone https://link-to-project
```

Go to the project directory

```cmd
  cd my-project
```

Install dependencies

```cmd
  pip install -r requirements.txt
```
Migrate the Database

```cmd
  python manage.py makemigrations
```
```cmd
  python manage.py migrate
```
To create Superuser/Admin 
```cmd
  python manage.py createsuperuser
```
Start the server
```cmd
  python manage.py runserver
```
Start redis server
```cmd
redis-server
```
Celery Command to run worker and celery beat 
Create new terminal to enter each below command
```cmd
celery -A proj_name worker --loglevel==INFO
celery -A proj_name beat --pool==solo
```

```cmd
 visit to http://localhost:8000/admin/
```
## Tech Stack

```
HTML5, CSS3, JS, TailwindCSS, Python, Django
Courier API, Celery, Redis
```

## Badges

[![MIT License](https://img.shields.io/github/license/Kunalp02/Crime_Reporting_Portal)](https://choosealicense.com/licenses/mit/)



