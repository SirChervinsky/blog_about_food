from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "created_at", "id"]
    inlines = [
        RecipeInline,
    ]


class RecipeAdmin (admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Comment)
