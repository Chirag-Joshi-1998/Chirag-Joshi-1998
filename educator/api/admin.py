from django.contrib import admin
from .models import Eductor
# Register your models here.

@admin.register(Eductor)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'number', 'city']