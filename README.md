# WHT
When have time. Do when have time.

# How to run

The fastest way to run the site is to run it in heroku. This should be enough for quickstart:

``` bash
git clone https://github.com/sberaccelerator/wht.git
cd wht
pip install -r requirements.txt
```

Create `.env` file in root directory and copy-paste this:
``` bash 
```

Run migrations to setup SQLite database:
``` bash
python manage.py migrate
```

Run service:
``` bash
heroku local -f Procfile.local -e .env
```

If you want to open Django admin panel which will be located on http://localhost:8000

## Deploy to Production 

Read Wiki page on how to [deploy on Heroku](https://devcenter.heroku.com/categories/command-line) scalable Telegram bot using Dokku.

# Creating Database

[url](https://lucid.app/lucidchart/42f68728-38fe-4d50-bb3c-b9002f541fc2/edit?invitationId=inv_6db45288-b5b2-4ace-839f-f882028227d1)

# MVP specification

- [ ] Хранение постов
    - [ ] Логотип вкладки
    - [ ] Ссылка 
    - [ ] Название вкладки
- [ ] Добавление ссылки
- [ ] Удаление поста
- [ ] Архивация 
- [ ] Двустраничный сайт (адаптированный под мобилки)

# Technical specification

- [ ] Превращение ссылки в пост (подробнее в проекте [Reading-Mode](https://github.com/sberaccelerator/Reading-Mode))
- [ ] Хранение постов по схеме из [:arrow_up:Creating Database](#CreatingDatabase)
    - [ ] Пост принадлежит каналу
    - [ ] Канал принадлежит человеку (может быть несколько админов)
- [ ] Работа с постами
    - [ ] Хранение истории просмотров
    - [ ] Возможность минимальной оценки поста (Лайки)
    - [ ] Режим помещения статьи в "Архив" (Возможно, с метками о времени)
    - [ ] Режим помежения статьи в "список чтения" (т.е. в ленту)
- [ ] Работа с каналами 
    - [ ] Возможность подписки
    - [ ] Вытаскивание rss ссылки из каждой статьи в мейнпуле и создание из нее канала (на  раннем этапе)
    - [ ] Меню подписок
    - [ ] Возможно, архивирование канала
    - [ ] Работа с rss
    - [ ] Асинхронная обработка rss
    - [ ] Балансировка в соответствии с нагрузкой сервера (мб многосерверная архитектура)
- [ ] Прасинг (пока без соцсетей, только rss каналы)
    - [ ] Извлечение в соответствии с планом из [Reading-Mode](https://github.com/sberaccelerator/Reading-Mode)
    - [ ] Парсинг rss лент с сайта
- [ ] Telegram bot для сохранения статей
- [ ] Адаптивность под мобилки и работа в режиме PWA
