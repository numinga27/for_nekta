# Тестовое задание для NEKTA
Создание наподопбие личного кабинета для завявок. Завявки видит только админ и автор завявок. 
Авторизация по токену 

## Ключевые возможности сервиса
* Создание заявки и вход в личный кабинет
* Узнать статус и найти свою завявку 
* http://127.0.0.1:8000/api/v1/requests/ — POST-запрос на создание новой заявки;
* http://127.0.0.1:8000/api-token-auth/ — POST-запрос на получение токена. Получить токен может только существующий пользователь
* Доступен api интерфейс.
## Технологии
* Python 3.11
* Postman
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:numinga27/for_nekta.git
```

```
cd nekta
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запуск проекта:

```
python manage.py runserver
```
## Автор: [Крылов Андрей][http://telegram.com/@numinga92]
