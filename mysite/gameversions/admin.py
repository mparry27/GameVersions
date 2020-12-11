from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Game)
admin.site.register(Console)
admin.site.register(ConsoleGame)
admin.site.register(ConsoleGamePositives)
admin.site.register(ConsoleGameNegatives)
