from django.contrib import admin
from .models import Task,ContextEntry

admin.site.register(Task)
admin.site.register(ContextEntry)