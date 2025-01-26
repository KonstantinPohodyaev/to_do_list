import re

from rest_framework.exceptions import ValidationError


INVALID_CHARS = r'[^\w.,_]'
INVALID_USERNAME_VALIDATION_ERROR = (
    'Недопустимые символы в поле username: {invalid_symbols}'
)


def username_validator(username):
    invalid_symbols = re.findall(INVALID_CHARS, username)
    if invalid_symbols:
        raise ValidationError(invalid_symbols=invalid_symbols)
    return username
