from django.contrib import admin
from .models import *

# Register your models here.

#注册后才能在admin中显示
admin.site.register(Publish)
admin.site.register(Book)