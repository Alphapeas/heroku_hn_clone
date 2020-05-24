
# App "News with Django3, DRF,Cron, Postgresql"
* Link to api working api: https://hidden-scrubland-22936.herokuapp.com/api/v1/news/
* Postman collection: https://www.getpostman.com/collections/1ebdf9fcc78aeb97838c
* You need add header "Authorization" in Postman app with value Token {token_that_you_take_from_login}
* Collection consist of variables like api_v1_url and all requests than you can do
##Local development
To run app in localhost you need to perform in work dir
```bash
$ git clone https://github.com/alphapeas/heroku_hn_clone.git
```
Than go to project dir, create virtual environment and get project packages
```bash
$ cd heroku_hn_clone
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
$ docker build -t registry.heroku.com/hidden-scrubland-22936/web .
```
Push your changes
```
$ docker push registry.heroku.com/hidden-scrubland-22936/web
```
Now release container to Heroku
```bash
$ heroku container:release -a hidden-scrubland-22936 web
```
Go to Heroku Dashboard and add Postgresql addon to your app, than apply migrations
```bash
$ heroku run python manage.py makemigrations -a hidden-scrubland-22936
$ heroku run python manage.py migrate -a hidden-scrubland-22936
```
App have been successfully deployed)