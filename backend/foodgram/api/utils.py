from django.http import HttpResponse
from datetime import datetime as dt


def download_cart(self, request, ingredients):
    user = self.request.user
    filename = f'{user.username}_shopping_list.txt'

    today = dt.today()
    shopping_list = (
        f'Список покупок для пользователя: {user.username}\n\n'
        f'Дата: {today:%Y-%m-%d}\n\n'
    )
    shopping_list += '\n'.join([
        f'- {ingredient["ingredient__name"]} '
        f'({ingredient["ingredient__measurement_unit"]})'
        f' - {ingredient["amount"]}'
        for ingredient in ingredients
    ])
    shopping_list += f'\n\nFoodgram ({today:%Y})'

    response = HttpResponse(
        shopping_list, content_type='text.txt; charset=utf-8'
    )
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response