from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import username_validator


TASK_NAME_VERBOSE_NAME = 'Название задачи'
TASK_NAME_MAX_LENGTH = 128
TASK_NAME_HELP_TEXT = 'Введите название задачи'

TASK_TEXT_VERBOSE_NAME = 'Цель задания'
TASK_TEXT_HELP_TEXT = 'Определите цель вашей задачи'

TASK_SLUG_VERBOSE_NAME = 'Уникальный slug'
TASK_SLUG_MAX_LENGTH = 64
TASK_SLUG_HELP_TEXT = 'Задайте задаче уникальный slug'

TASK_DONE_STATUS_VERBOSE_NAME = 'Статус задачи'

TASK_OVERDUE_STATUS_VERBOSE_NAME = 'Просрочено'

TASK_START_DATE_VERBOSE_NAME = 'Время создания задачи'

TASK_END_DATE_VERBOSE_NAME = 'Срок сдачи задачи'
TASK_END_DATE_HELP_TEXT = (
    'Укажите дату, к которой нужно заверщить эту задачу'
)

TASK_META_VERBOSE_NAME = 'задача'
TASK_META_VERBOSE_NAME_PLURAL = 'Задачи'

CUSTOM_USER_USERNAME_VERBOSE_NAME = 'Юзернейм'
CUSTOM_USER_USERNAME_MAX_LENGTH = 64
CUSTOM_USER_USERNAME_HELP_TEXT = (
    'Придумайте уникальный юзернейм для пользователя'
)

CUSTOM_USER_EMAIL_VERBOSE_NAME = 'Адрес электронной почты'
CUSTOM_USER_EMAIL_MAX_LENGTH = 128
CUSTOM_USER_EMAIL_HELP_TEXT = (
    'Введите уникальный адрес электронной почты'
)

CUSTOM_USER_FIRST_NAME_VERBOSE_NAME = 'Имя'
CUSTOM_USER_FIRST_NAME_MAX_LENGTH = 64
CUSTOM_USER_FIRST_NAME_HELP_TEXT = 'Введите ваше имя'

CUSTOM_USER_LAST_NAME_VERBOSE_NAME = 'Имя'
CUSTOM_USER_LAST_NAME_MAX_LENGTH = 64
CUSTOM_USER_LAST_NAME_HELP_TEXT = 'Введите ваше имя'

CUSTOM_USER_BIO_VERBOSE_NAME = 'Биография'
CUSTOM_USER_BIO_HELP_TEXT = 'Введите биографию'

CUSTOM_USER_VERBOSE_NAME = 'пользователь'
CUSTOM_USER_VERBOSE_NAME_PLURAL = 'Пользователи'


class CustomUser(AbstractUser):
    username = models.CharField(
        CUSTOM_USER_USERNAME_VERBOSE_NAME,
        max_length=CUSTOM_USER_USERNAME_MAX_LENGTH,
        validators=[username_validator,],
        unique=True,
        help_text=CUSTOM_USER_USERNAME_HELP_TEXT
    )
    email = models.EmailField(
        CUSTOM_USER_EMAIL_VERBOSE_NAME,
        unique=True,
        max_length=CUSTOM_USER_EMAIL_MAX_LENGTH,
        help_text=CUSTOM_USER_EMAIL_HELP_TEXT
    )
    first_name = models.CharField(
        CUSTOM_USER_FIRST_NAME_VERBOSE_NAME,
        max_length=CUSTOM_USER_FIRST_NAME_MAX_LENGTH,
        help_text=CUSTOM_USER_FIRST_NAME_HELP_TEXT
    )
    last_name = models.CharField(
        CUSTOM_USER_LAST_NAME_VERBOSE_NAME,
        max_length=CUSTOM_USER_LAST_NAME_MAX_LENGTH,
        help_text=CUSTOM_USER_LAST_NAME_HELP_TEXT
    )
    bio = models.TextField(
        CUSTOM_USER_BIO_VERBOSE_NAME,
        null=True,
        help_text=CUSTOM_USER_BIO_HELP_TEXT
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = CUSTOM_USER_VERBOSE_NAME
        verbose_name_plural = CUSTOM_USER_VERBOSE_NAME_PLURAL
        ordering = ['username', 'last_name', 'first_name']


class Task(models.Model):
    name = models.CharField(
        TASK_NAME_VERBOSE_NAME,
        max_length=TASK_NAME_MAX_LENGTH,
        unique=True,
        help_text=TASK_NAME_HELP_TEXT
    )
    text = models.TextField(
        TASK_TEXT_VERBOSE_NAME,
        blank=True,
        null=True,
        help_text=TASK_TEXT_HELP_TEXT
    )
    slug = models.SlugField(
        TASK_SLUG_VERBOSE_NAME,
        max_length=TASK_SLUG_MAX_LENGTH,
        unique=True,
        help_text=TASK_SLUG_HELP_TEXT
    )
    done_status = models.BooleanField(
        TASK_DONE_STATUS_VERBOSE_NAME,
        blank=True,
        default=False
    )
    start_date = models.DateTimeField(
        TASK_START_DATE_VERBOSE_NAME,
        auto_now_add=True
    )
    end_date = models.DateTimeField(
        TASK_END_DATE_VERBOSE_NAME,
        help_text=TASK_END_DATE_HELP_TEXT
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = TASK_META_VERBOSE_NAME
        verbose_name_plural = TASK_META_VERBOSE_NAME_PLURAL
        ordering = ['start_date', 'slug', 'name']
        default_related_name = 'tasks'
