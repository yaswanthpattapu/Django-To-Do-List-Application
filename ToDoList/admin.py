from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


@admin.register(ListModel)
class ListAdmin(admin.ModelAdmin):
    fields = ['Title', 'Description', 'DueDate', 'Tag', 'Status']
    createonly_fields = ['Description','Status']
    list_filter = ('Timestamp', 'DueDate', 'Tag', 'Status')
    list_display = (
        "id",
        "Title",
        "Description",
        "Timestamp",
        "DueDate",
        "tags",
        "Status",
    )


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ("id", "title")
