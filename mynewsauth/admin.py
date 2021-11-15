from django.contrib import admin

from news.models import StoredNews
from .models import CustomUserModel

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(StoredNews)