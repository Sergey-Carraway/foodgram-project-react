from io import BytesIO

from django.http import FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from api.serializers import RecipeIngredients


def download_cart(request):
    ingredients = RecipeIngredients.objects.filter(
        recipe__shopping__user=request.user
    ).values_list("ingredient__name", "ingredient__measurement_unit", "amount")
    cart_list = {}
    for item in ingredients:
        name = item[0]
        if name not in cart_list:
            cart_list[name] = {"measurement_unit": item[1], "amount": item[2]}
        else:
            cart_list[name]["amount"] += int(item[2])
    height = 700
    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont("arial", "static/arial.ttf"))
    page = canvas.Canvas(buffer)
    page.setFont("arial", 13)
    page.drawString(100, 750, "Список покупок")
    for i, (name, data) in enumerate(cart_list.items(), start=1):
        page.drawString(
            80, height,
            f"{i}. {name} – {data['amount']} {data['measurement_unit']}"
        )
        height -= 25
    page.showPage()
    page.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True,
                        filename="shopping_list.pdf")
