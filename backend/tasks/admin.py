from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'status', 'user')
    list_display_links = ('id', 'title')
    list_editable = ('status',)
    search_fields = ('title', 'start_date')
    list_per_page = 25


admin.site.register(Task, TaskAdmin)
