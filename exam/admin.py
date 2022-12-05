from django.contrib import admin

# Register your models here.
from .models import Course,Result,Question
myModels = [Course,Result,Question]
admin.site.register(myModels)