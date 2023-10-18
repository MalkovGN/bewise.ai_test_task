### Тестовое задание
API реализовано при помощи фреймворка FastAPI;
В качестве БД использована PostgreSQL;
ORM - SQLAlchemy, миграции - Alembic.

***Инструкция для запуска***
1. Склонировать репозиторий `git clone https://github.com/MalkovGN/bewise.ai_test_task`
2. Перейти в папку проекта, для запуска использовать комманду `docker-compose up -d`
3. Перейти в браузере по адресу `http://127.0.0.1:8008/docs/` для просмотра Swagger документации.
  
  Тестовые запросы можно отправлять из Swagger или же через Postman по указанному URL.<br>
         
  ***Остановить и удалить контейнер***        
   1. `docker-compose stop`          
   2. `docker-compose down -v`   
