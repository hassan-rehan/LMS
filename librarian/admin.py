from django.contrib import admin
from .models import book, book_category
import pdb



class MyModelAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/custom_admin.js',)

    exclude = ["clicks"]
    search_fields = ['title','asin_no']
    list_filter = ['created_at']
    list_per_page = 50 # No of records per page
    ordering = ['-created_at']

admin.site.register(book_category)
admin.site.register(book, MyModelAdmin)