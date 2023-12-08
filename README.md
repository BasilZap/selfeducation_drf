# Дипломная работа "OB1. Проект самообучения".

## Функционал.
Платформа SelfEDU создана с помощью Django Rest Framework и работает с СУБД PostgreSQL,
с полями таблиц "Раздел", "Материал", "Тестовый вопрос", "Тестовый ответ" "Пройденный тест",
для которых созданы и описаны соответствующие модели. Созданы отображения 
и фильтры для таблиц в панели администратора Django. Созданы вьюсеты и сериализаторы для
обработки запросов от пользователя. Дополнительно созданы пользовательские представления
для обработки ответов пользователей на тестовые вопросы непосредственно на сервере.
Управление всеми сущностями реализовано через стандартный Django admin.

Проходить обучение, и тесты могут только зарегистрированные пользователи.

- ### Регистрация пользователя.
Регистрация (для локальной версии) осуществляется по следующему адресу:
http://127.0.0.1:8000/users/register/
отправкой POST-запроса вида:
```
{
    "email": "ivan@ivanov.ru",
    "password": "123"
}
```
с указанием своего e-mail и пароля.

- ### Получение списка разделов.
Получить список разделов можно с помощью GET-запроса по адресу:
http://127.0.0.1:8000/

- ### Получение содержания раздела со списком материалов.
Получить содержимое раздела можно с помощью GET-запроса по адресу:
http://127.0.0.1:8000/chapter/5/
где 5 - id раздела

- ### Получение содержания материала со списком тестовых вопросов и ответов на них.
Получить содержимое раздела можно с помощью GET-запроса по адресу:
http://127.0.0.1:8000/material/8/
где 8 - id материала

- ### Получение содержания конкретного тестового вопроса и списка ответов на него.
Получить содержимое раздела можно с помощью GET-запроса по адресу:
http://127.0.0.1:8000/question/6/
где 6 - id вопроса


- ### Ответы на тестовые вопросы.
Предусмотрено два варианта проверки ответов на тестовые вопросы:

- Вариант 1 - Проверка ответа на один, конкретный вопрос производится по адресу: http://127.0.0.1:8000/test/ 
путем отправки POST-запроса в формате:
```
{
    "id": 2,
    "answers": [
        {
            "id": 4
        },
        {
            "id": 5
        }
    ]
}
```

,где "id": 2 - это id вопроса, а [{"id": 4},{"id": 5}] - это id "правильных" вариантов ответа.
#### Как можно заметить - на один вопрос может быть несколько правильных вариантов ответа

- Вариант 2 - Проверка ответов на несколько/все вопросы материала производится по адресу: http://127.0.0.1:8000/tests/
путем отправки POST-запроса в формате:
```
{
    "answers": [
        {
            "id": 3,
            "answers": [
                {
                    "id": 13
                }
            ]
        },
        {
            "id": 4,
            "answers": [
                {
                    "id": 9
                },
                {
                    "id": 10
                },
                {
                    "id": 8
                }
            ]
        }
    ]
}
```
,где, как и в предыдущем случае "id": 3 и "id": 4 - это id вопросов, а во вложенных списках id ответов.

В случае корректного ввода данных пользователь получит ответ в виде:
```
{
    "3": {
        "success": true,
        "is_true": true,
        "hint": "Ответ верный"
    }
}
```
"success" - выполнено без ошибок - True
"is_true" - пользователь дал правильный ответ - True
"hint" - расшифровка

В случае, если данные введены некорректно, пользователь получит ответ вида:
```
{
    "2": {
        "success": false,
        "hint": "Проверьте правильность наименования ключей ('id', 'answers')"
    }
}
```

- ### Добавление материалов
Добавление материалов осуществляется администратором через панель администратора django


## Требования к установке.
- В PostgreSQL должна быть создана DB - selfedu
- Необходимо заполнить таблицы БД значениями

Заполнение базы осуществляетя через команды:
- Суперпользователь
```
> python manage.py ucreate
```
Для заполнения БД тестовыми данными необходимо воспользоваться фикстурой all.json
```
> python manage.py loaddata all.json
```


## Требования к окружению

#### В программе используется менеджер зависимостей venv.
Используются следующие зависимости:

- Django==4.2.4
- ipython==8.14.0
- Pillow==10.0.0
- psycopg2-binary==2.9.7
- pytils==0.4.1
- django-cors-headers==4.3.1
- django-debug-toolbar==4.2.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.0
- drf-yasg==1.21.7
- python-dotenv==1.0.0
