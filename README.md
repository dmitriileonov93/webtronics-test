# Тестовое задание для Webtronics

### Задание:
Object of this task is to create a simple REST API. You have to use Django and
Django rest framework.

SOCIAL NETWORK

Basic models:
• User
• Post (always made by a user)
Basic features:
• user signup
• user login
• post creation
• post like
• post unlike

For User and Post objects, candidate is free to define attributes as they see fit.

Requirements:
• Token authentication (JWT is prefered)
• use Django with any other Django batteries, databases etc.

Optional (will be a plus):
• use clearbit.com/enrichment for getting additional data for the user on signup
• use emailhunter.co for verifying email existence on signup

### Описание:
Проект реализован в 3х docker контейнерах:
- db (PostgreSQL)
- nginx
- web (DRF, Gunicorn)

Документация API доступна после запуска проекта по эндпоинту '/api/v1/redoc/'

### Запуск проекта:
- Для загрузки введите в командную строку:
```
git clone https://github.com/dmitriileonov93/webtronics-test.git
```
- Перейти в корневую папку проекта:
```
cd webtronics-test/
```
- Создайте файл .env для переменных окружения в папке в файлом settings.py:
```
touch social_network/social_network/.env
```
- Добайте в этот файл переменные окружения:
```
echo <ПЕРЕМЕННАЯ>=<значение> >> social_network/social_network/.env
```
- Запуск приложения из корневой папки проекта:
```
docker-compose up -d --build
```
Для упрощения процесса тестирования проект уже имеет фикстуры в БД и суперпользователя.
