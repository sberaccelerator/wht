# WHT
When have time. Do when have time. Deferred reading service.

# How to run
## Quickstart

## Run locally using heroku CL
## Установка пакетов
Далее необходимо на это виртуальное окружение накинуть пакеты. Я для этого в VS Code открываю новую консольку, вижу надпись (.venv), ввожу команду:
```
    pip install -r requirements.txt
```
## Запуск
```
    heroku local -f Procfile.local
```

## Deploy to Production 

# TODO list
### IgorVoron
- [ ] Finish README.MD
- [ ] Finish database engineering
- [ ] Write Docs
### viktor-strebulaev
- [ ] Write models 
### IrinaKlo
- [ ] [Reading Mode](https://github.com/sberaccelerator/Reading-Mode)


# django-telegram-bot
Django + python-telegram-bot + Celery + Redis + Postgres + Dokku + GitHub Actions template. Production-realy Telegram bot with database, admin panel and a bunch of useful built-in methods.

### Check the example bot that uses the code from Main branch: [t.me/djangotelegrambot](https://t.me/djangotelegrambot)

## Features

* Database: Postgres, Sqlite3, MySQL - you decide!
* Admin panel (thanks to [Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/))
* Background jobs using [Celery](https://docs.celeryproject.org/en/stable/)
* [Production-ready](https://github.com/ohld/django-telegram-bot/wiki/Production-Deployment-using-Dokku) deployment using [Dokku](https://dokku.com)
* Telegram API usage in pooling or [webhook mode](https://core.telegram.org/bots/api#setwebhook)

Built-in Telegram bot methods:
* /broadcast - send message to all users (admin command)
* /stats - show basic bot stats 
* /ask_for_location - log user location when received and reverse geocode it to get country, city, etc.
* Log users clicks to understand their behaviour

Check out our [Wiki](https://github.com/ohld/django-telegram-bot/wiki) for more info.

# How to run

## Quickstart: Pooling & SQLite

The fastest way to run the bot is to run it in pooling mode using SQLite database without all Celery workers for background jobs. This should be enough for quickstart:

``` bash
git clone https://github.com/ohld/django-telegram-bot
cd django-telegram-bot
pip install -r requirements.txt
```

Create `.env` file in root directory and copy-paste this:
``` bash 
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
TELEGRAM_TOKEN=<ENTER YOUR TELEGRAM TOKEN HERE>
```

Run migrations to setup SQLite database:
``` bash
python manage.py migrate
```

Run bot in pooling mode:
``` bash
python run_pooling.py 
```

If you want to open Django admin panel which will be located on http://localhost:8000/tgadmin/:
``` bash
python manage.py runserver
```

## Run locally using docker-compose

If you like docker-compose you can check [full instuctions in our Wiki](https://github.com/ohld/django-telegram-bot/wiki/Run-locally-using-Docker-compose).

## Deploy to Production 

Read Wiki page on how to [deploy production-ready](https://github.com/ohld/django-telegram-bot/wiki/Production-Deployment-using-Dokku) scalable Telegram bot using Dokku.

----
