# SimpleDjangoDocker

This is just a simple project to try out some cool stuff, e.g. Django, Docker, Celery and many other things, that I come up to.

## Settings

In order to make this thing work, you have to create ```.env``` folder and add ```.django``` and ```.postgres``` inside it.
It should look like this:


    .
    ├── ...
    ├── .env                    # env folder
    │   ├── .django             # env for django
    │   └── .postgres           # env for postgres
    └── ...

| .django | .postgres |
|----------|----------|
|DJANGO_SECRET_KEY|POSTGRES_HOST|
|DJANGO_EMAIL_BACKEND|POSTGRES_DB|
|DJANGO_DEFAULT_FROM_EMAIL|POSTGRES_USER|
|DJANGO_EMAIL_HOST|POSTGRES_PASSWORD|
|DJANGO_EMAIL_HOST_USER|
|DJANGO_EMAIL_HOST_PASSWORD|
|DJANGO_EMAIL_PORT|
|CELERY_BROKER_URL|

## Start

Simply use this command to start this awesome project
```
$ docker-compose up
```
