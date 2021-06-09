from django.contrib import admin

from .models import User, Task

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')

@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','assign_to')
