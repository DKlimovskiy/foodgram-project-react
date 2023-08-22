# praktikum_new_diplom
перейти в папку infra:
 cd infra

выполнить команду:
 sudo docker-compose up -d

после завершения сборки контейнеров запустить миграции:
 sudo docker exec -it infra-backend-1 python manage.py migrate

создать суперпользователя:
 sudo docker exec -it infra-backend-1 python manage.py createsuperuser

добавить ингридиенты в базу данных:
 sudo docker exec -it infra-backend-1 python manage.py loaddata data/ingredients.json

перейти на страницу сайта http://127.0.0.1/ 
перейти в админку http://127.0.0.1/admin