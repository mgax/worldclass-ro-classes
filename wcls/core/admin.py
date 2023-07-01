from django.contrib import admin

from .models import Club, Class


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["__str__", "sync"]


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ["__str__", "club", "day", "hours", "trainers"]
