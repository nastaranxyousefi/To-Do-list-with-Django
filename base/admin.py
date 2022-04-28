from django.contrib import admin

from .models import Task

@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'complete', 'created',)


