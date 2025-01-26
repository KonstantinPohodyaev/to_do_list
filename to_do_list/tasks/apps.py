from django.apps import AppConfig


NAME = 'tasks'
VERBOSE_NAME = 'Задачи'


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = NAME
    verbose_name = VERBOSE_NAME
