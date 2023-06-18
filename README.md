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
### **Запуск проекта на сервере в контейнерах:**
```
# МЕНЯЕМ БАЗУ SQLITE НА POSTGRES
pip install python-dotenv
# ИЗМЕНЯЕМ НАСТРОЙКИ БД В settings.pe
docker build -t serzhkaravaev/foodgram_frontend . # Собрали образ foodgram_frontend
docker build -t serzhkaravaev/foodgram_backend . # Собрали образ foodgram_backend
docker push serzhkaravaev/foodgram_frontend # Запушили DockerHub
docker push serzhkaravaev/foodgram_backend # Запушили DockerHub
ssh serzh-karavaev@158.160.4.227 # Заходим на ВМ
mkdir Dev # Создаем директорию Dev
cd Dev/ # Переходим Dev
mkdir footgram # Создаем директорию  footgram
scp -r infra serzh-karavaev@158.160.4.227:/home/serzh-karavaev/Dev/foodgram # Копируем infra/ на сервер
scp -r docs serzh-karavaev@158.160.4.227:/home/serzh-karavaev/Dev/foodgram # Копируем docs/ на сервер
# ПИШЕМ foodgram.yml
sudo systemctl stop nginx
git add .
git commit -m""
git push
```

---

### **шаблон наполнения env-файла**

```
DB_HOST=db
DB_PORT=5432
DB_ENGINE=django.db.backends.postgresql
POSTGRES_PASSWORD=serzh
POSTGRES_USER=postgres
POSTGRES_DB=postgres
SECRET_KEY="django-insecure-$(6k__+o93&uy@iiwzp&15*q)1bg9xy+x!0gl$7x@q-#e-&pe-"

```
---
### **Actions secrets**

```
DB_ENGINE
DB_HOST
DB_NAME
DB_PORT
DOCKER_PASSWORD
DOCKER_USERNAME
HOST
POSTGRES_PASSWORD
POSTGRES_USER
SECRET_KEY
SSH_KEY
TELEGRAM_TO
TELEGRAM_TOKEN
USER

```

---

### **Спецификация API Foodgram**
Документация: http://localhost/api/docs/

---

### **Сайт**

http://158.160.4.227/signin
