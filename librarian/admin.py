from django.contrib import admin
from .models import book, book_category, reservation

admin.site.register(book_category)
admin.site.register(reservation)
admin.site.register(book)