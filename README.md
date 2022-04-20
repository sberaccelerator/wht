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
