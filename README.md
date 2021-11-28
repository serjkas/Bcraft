# Установка


## Для локальной разработки создать виртуальное окружение:
Windows
```
> python -m venv venv
> source venv\bin\activate
```
Linux
```
$ virtualenv venv
$ source venv/bin/activate
```
## Создать базу и пользователя
```
create user admin with password 'admin';
alter role admin set client_encoding to 'utf8';
alter role admin set default_transaction_isolation to 'read committed';
alter role admin set timezone to 'UTC';
```	
```	
create database fr_db owner admin;
```
Заменить в `setting.py`-`DATABASE`. Заменить данные для подключения на `admin` 
## Установить зависимости из файла:

```
(venv) pip install -r requirements.txt
```
`(venv)` Вначале строки.Это виртуальное окржение из  `virtualenv2` или `python -m venv`.

Как только `pip` завершит установку:
```
(env)$ cd src/
(env)$ python manage.py runserver
```
Стандартный путь `http://127.0.0.1:8000/`.

## Docker:
```docker compose up --build```

Для загрузки первых данных:
```docker exec -it <container_name> bash```
Загружаем данные
```python manage.py loaddata ../fixtures/activity.json```

# Описание

## Для получения списка статистики, метод `GET`:
```http://127.0.0.1:8000/api/v1/activity/?from=YYYY-MM-DD&to=YYYY-MM-DD```.`YYYY-MM-DD`, прим. 2021-11-28
`&ordering=<paramentr>` - это допольнительный параметр для сортировки по полю, поля можно выбирать любые из модели. Без параметра идет сортировка по `дате`, по умолчанию


## Создание записи, метод `POST`:
Используем `POST` запрос с `JSON`, вида:
`
{
        "views": 3,
        "clicks": 2,
        "cost": 1
}
`
Ссылка: ```http://127.0.0.1:8000/api/v1/activity/```
В ответ получаем созданный объект с `cpc`, `cpm`.

## Удаление статистики, метод `DELETE`:
Используем метод `DELETE`. Удалит всю статистику.
Ссылка: ```http://127.0.0.1:8000/api/v1/delete_statistics```




