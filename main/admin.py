from django.contrib import admin
from .models import Author, Book, Article

admin.site.register([Author, Book, Article])