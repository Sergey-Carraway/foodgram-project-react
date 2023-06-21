import datetime as dt

from django.core.exceptions import ValidationError


def validate_username(value):
    """Валидатор username"""

    if value.lower() == "me":
        raise ValidationError(
            ("Имя пользователя не может быть <me>."),
            params={"value": value},
        )


def validate_year(value):
    """Валидатор date"""

    year = dt.date.today().year
    if not (value <= year):
        raise ValidationError("Дата указана некорректно!")
    return value


def validate_amount(value):
    if value <= 0:
        raise ValidationError("Колличество должно быть больше 0")
    return value


def validate_cooking_time(value):
    if value is None:
        raise ValidationError("Нужно написать время приготовления")
    if value <= 0:
        raise ValidationError("Приготовление занимает не менее 1 мин")
    return value
