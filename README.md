# Instrukcja
- sudo docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=pass -e MYSQL_DATABASE=test -p 3306:3306 -d mysql
- Git pull
- pip3 install -r requirements.txt --user
- ./manage.py migrate (from folder with manage.py)
- ./manage.py runserver
- open in browser  http://127.0.0.1:8000/


or if u wanna change settings for database you can do it in todolistproject/todolistproject/settings.py 