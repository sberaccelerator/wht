# WHT
When have time. Do when have time. Сервис отложенного чтения.

# Как запустить?
## Создание виртуального окружения
```
    python -m venv .venv
```
## Запуск виртуального окружения
Запускаем сценарий:
```
    .venv\Scripts\activate.bat
```
## Установка пакетов
Далее необходимо на это виртуальное окружение накинуть пакеты. Я для этого в VS Code открываю новую консольку, вижу надпись (.venv), ввожу команду:
```
    pip install -r requirements.txt
```
## Запуск
```
    heroku local -f Procfile.local
```
