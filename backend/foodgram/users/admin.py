from django.contrib import admin
from foodgram.settings import EMPTY_VALUE_DISPLAY

from users.models import Follow, User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "password",
    )
    search_fields = (
        "username",
        "email",
    )
    list_filter = (
        "username",
        "email",
    )
    empty_value_display = EMPTY_VALUE_DISPLAY

    @admin.display(description='Рецепты пользователя')
    def recipe_count(self, obj):
        return obj.recipes.count()

    @admin.display(description='Подписчики пользователя')
    def follows_count(self, obj):
        return obj.following.count()


@admin.register(Follow)
class FolowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "author")
    search_fields = ["user", "author__username"]
