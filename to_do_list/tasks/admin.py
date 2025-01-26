from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Task, CustomUser

admin.site.unregister(Group)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ...