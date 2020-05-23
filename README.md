
# App "News with Django3, DRF,Cron, Postgresql"
* Link to api working api: http://boiling-oasis-95257.herokuapp.com/api/v1/post/list/
* Postman collection: https://www.getpostman.com/collections/1ebdf9fcc78aeb97838c
(Collection consist of variables like api_v1_url and all requests than you can do to app)
##Local development
To run app in localhost you need to perform in work dir
```bash
$ git clone https://github.com/alphapeas/heroku_news.git
```
Than go to project dir, create virtual environment and get project packages
```bash
$ cd heroku_news
$ python3.7 -m venv env
$ pip install -r requirements.txt
```
Now you need to make migrations and migrate
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
Finally you can run app into http://localhost:8000
```bash
$ python manage.py runserver
```

##Push changes to Heroku
Connect to Heroku
```bash
$ heroku login
$ heroku container:login
```
You need to rebuilt Docker container, go to project root and run:
```
$ docker build -t registry.heroku.com/boiling-oasis-95257/web .
```
Push your changes
```
$ docker push registry.heroku.com/boiling-oasis-95257/web
```
Now release container to Heroku and run migrations
```bash
$ heroku container:release -a boiling-oasis-95257 web
$ heroku run python manage.py makemigrations -a boiling-oasis-95257
$ heroku run python manage.py migrate -a boiling-oasis-95257
```