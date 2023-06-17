### **Описание проекта:**
сайт **Foodgram** - «Продуктовый помощник» <br>
На этом сервисе пользователи смогут <br> 
- публиковать рецепты <br>
- подписываться на публикации других пользователей <br>
- добавлять понравившиеся рецепты в список «Избранное»<br>
- скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

--- 

### **Запуск проекта локально в контейнерах:**
```
git clone git@github.com:Sergey-Carraway/foodgram-project-react.git
git # клонируем проект
python -m venv venv # Создаем виртуальное окружение
source /venv/Scripts/activate # Активируем виртуальное окружение
cd infra/ # Переходим в папку infra/
docker-compose up # Запуск docker-compose (Документация доступна по адресу http://localhost/api/docs/)
cd backend/ # Переходим в папку backend/ , здесь мы пишем бэк
django-admin startproject foodgram # Создаем основу проекта
python manage.py startapp api # Создаем приложение api
python manage.py startapp users # Создаем приложение users
python manage.py startapp recipes # Создаем приложение recipes
# ПИШЕМ ПРОЕКТ СОГЛАСНО ДОКУМЕНТАЦИИ
# ПРОВЕРЯЕМ ВСЕ РУЧКИ В POSTMAN
pip install gunicorn # Устанавливаем gunicorn
# Дописываем docker-compose.yaml
# Дописываем nginx.conf
docker compose up --build # Собираем образы и контейнеры
# Открываем второй терминал
docker ps # Смотрим какие контейнеры ест
docker exec -it id bash # Попадаем внутрь контейнера 
python manage.py collectstatic # Собираем статику в контейнере
# ТЕСТИМ ПРОЕКТ ЛОКАЛЬНО ВНУТРИ РАБОТАЮЩИХ КОНТЕЙНЕРОВ
```
---
