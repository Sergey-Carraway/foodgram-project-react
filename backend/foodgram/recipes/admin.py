from django.contrib import admin

from recipes.models import (Favourite, Ingredient, Recipe, RecipeIngredients,
                            ShoppingCart, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "color", "slug")
    search_fields = ("name", "color", "slug")
    list_filter = ("name", "color", "slug")


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "measurement_unit")
    search_fields = ("name", "measurement_unit")
    list_filter = ("name", "measurement_unit")


class RecipeIngredientsInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "author", "text", "cooking_time", "image",
                    "date", "favarite_count")
    search_fields = ("name", "author__username", "text", "cooking_time",)
    list_filter = ("name", "author__username", "tags")
    readonly_fields = ("favarite_count",)
    inlines = (RecipeIngredientsInLine,)

    @admin.display(description="Количество избранных")
    def favarite_count(self, obj):
        """Получаем количество избранных"""
        return obj.favorites.count()

    favarite_count.short_description = "Количество избранных"


@admin.register(RecipeIngredients)
class RecipeIngridientsAdmin(admin.ModelAdmin):
    list_display = ("pk", "recipe", "ingredient", "amount")
    search_fields = ("recipe__name", "ingredient__name")
    list_filter = ("recipe", "ingredient")


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )
    search_fields = (
        "user__username",
        "recipe__name",
    )


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
    )
    search_fields = (
        "user__username",
        "recipe__name",
    )
