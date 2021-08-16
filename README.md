# Homework 20. Django Rest Framework
Жду ссылки на репозитории с проектом использующим DRF.

В проекте реализовать:

- минимум 2 модели с связями (Пост, Комментарий)
- модели поста и Комментария должны принадлежать пользователю (FK связь)
- сериализаторы для этих моделей
- CRUD использующий viewset для работы с этими моделями так, что бы:
- просматривать посты и комментарии могли все
- добавлять посты и комментарии могли только залогиненные пользователи
- изменять или удалять посты или комментарии могли только их владельцы (при удалении поста все комментарии удаляются вне зависимости от их владельцов)
- при желании можете использовать аутентификацию по токену

Cсылки:

https://www.django-rest-framework.org/api-guide/authentication/
https://dj-rest-auth.readthedocs.io/en/latest/index.html
https://dj-rest-auth.readthedocs.io/en/latest/installation.html
https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional
https://django-allauth.readthedocs.io/en/latest/installation.html