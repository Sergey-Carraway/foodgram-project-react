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


def validate_ingredients(self, value):
    if not value:
        raise ValidationError("Нужно добавить ингридиент.")
    for item in value:
        if item["amount"] <= 0:
            raise ValidationError("Колличество должно быть больше 0")
    return value


def validate_time(self, value):
    if not value:
        raise ValidationError("Нужно написать примерное время приготовления")
    for item in value:
        if item["amount"] <= 0:
            raise ValidationError("Каждое приготовление должно занимать не меньше 1 минуты")
    return value
