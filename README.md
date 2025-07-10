# API для Yatube  
Учебный проект по реализации RESTful API для социальной сети блогов.  


## Стек:
Python, Django, Django REST Framework (DRF), JWT (JSON Web Tokens) для аутентификации  

## Запуск отладочного сервера:
- Склонировать репозиторий:
```commandline
git clone git@github.com:Oryshich/api-final-yatube.git
```
В директории с проектом
- Создание виртуального окружения:
```commandline
python -m venv venv
```
- Активация виртуального окружения:
```commandline
source venv\Scripts\activate  
```
- Обновить pip:
```commandline
python3 -m pip install --upgrade pip
```
- Установка зависимостей:
```commandline
pip install -r requirements.txt
```
- Выполнить миграции:
```
python3 yatube_api/manage.py migrate
```
- Запуск отладочного сервера:
```commandline
cd yatube_api
python manage.py runserver
```

## Задача  
В проекте api_yatube есть приложение posts с описанием моделей Yatube.
Реализовано API для всех моделей приложения (в приложении **api**).

В проекте 
использована аутентификация по JWT-токену.  

Аутентифицированный пользователь авторизован на изменение и удаление своего контента; 
в остальных случаях доступ предоставляется только для чтения. 

## Реализованы следующие эндпоинты:
```api/v1/posts/``` : получаем список всех постов с использованием параметров limit и offset.
``` 
Пример ответа на запрос http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=1:
{
    "count": 2,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=1",
    "results": [
        {
            "id": 2,
            "author": "regular_user",
            "text": "Пост с группой",
            "pub_date": "2025-07-10T00:36:16.660191+03:00",
            "image": null,
            "group": 1
        }
    ]
}
```  
```api/v1/posts/{post_id}/``` : получаем, редактируем или удаляем пост с идентификатором ```{post_id}``` (для авторизированных пользователей).
```
Пример ответа на запрос http://127.0.0.1:8000/api/v1/posts/1/:
{
    "id": 1,
    "author": "regular_user",
    "text": "Пост зарегистрированного пользователя.",
    "pub_date": "2025-07-10T00:36:16.564185+03:00",
    "image": null,
    "group": null
}
``` 
```api/v1/groups/``` : получаем список всех групп.  
```
Пример ответа на запрос http://127.0.0.1:8000/api/v1/groups/:
[
    {
        "id": 1,
        "title": "TestGroup",
        "slug": "test-group",
        "description": "Some text."
    }
]
```
```api/v1/groups/{group_id}/``` : получаем информацию о группе с идентификатором ```{group_id}```.  
```
Пример ответа на запрос http://127.0.0.1:8000/api/v1/groups/1/:
{
    "id": 1,
    "title": "TestGroup",
    "slug": "test-group",
    "description": "Some text."
}
```
```api/v1/posts/{post_id}/comments/```  создаём новый комментарий/получаем комментарий для поста с идентификатором ```{post_id}```.   
```
Пример ответа на запрос http://127.0.0.1:8000/api/v1/posts/2/comments/:
{
    "id": 1,
    "author": "regular_user",
    "text": "Тестовый комментарий",
    "created": "2025-07-10T00:36:17.235347+03:00",
    "post": 2
}
```

## Над проекто работали  

* разработчик: **Орышич Евгений** (_109_ когорта)  
* ревьюер: **Шкода Игорь**  


<!-- Спринт 14 -->
