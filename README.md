# VektorGo Backend 🚀

API-сервер для локального маркетплейса **VektorGo** (Кусары и Северный регион Азербайджана). 
Обеспечивает работу базы данных, обработку объявлений, аутентификацию пользователей и сокет-соединения для чатов в реальном времени.

---

### 🛠 Технологический стек

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

* **Python / Django** — основной фреймворк и REST API
* **PostgreSQL** — основная реляционная база данных
* **Redis + Daphne** — брокер сообщений и ASGI-сервер для WebSockets (чаты)
* **Docker & Docker Compose** — контейнеризация и деплой

---

### 🚀 Локальный запуск (через Docker)

**1. Склонируйте репозиторий:**
```bash
git clone [https://github.com/dr-Panakhov/vektorgo-backend.git](https://github.com/dr-Panakhov/vektorgo-backend.git)
cd vektorgo-backend
```
**2. Настройте переменные окружения**
```bash
# Скопируйте шаблон .env.example в рабочий .env и пропишите доступы к БД и секретные ключи
cp .env.example .env
```
**3. Поднимите контейнеры**
```bash
docker-compose up -d --build
```
**4. Примените миграции**
```bash
docker exec -it my_backend python manage.py migrate
```
### 📦 Деплой на сервер (Production)

**Проект настроен для бесшовного деплоя на VPS (Debian/Ubuntu) с использованием готовых образов и docker-compose. Все контейнеры имеют политику restart: unless-stopped.**
