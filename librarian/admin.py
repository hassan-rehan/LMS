from django.contrib import admin
from .models import book, book_category

admin.site.register(book_category)
admin.site.register(book)