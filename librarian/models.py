from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'books/cover'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(str(instance.pk)+"_p", ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class CategoryField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(CategoryField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class book_category(models.Model):
    category = CategoryField(max_length=100)

class book(models.Model):
    description = models.TextField()
    cover_pic = models.ImageField(upload_to=path_and_rename)
    title = models.CharField(max_length=100)
    category_id = models.ForeignKey(book_category,db_column="category_id", on_delete=models.CASCADE)
    reserved_by = models.ForeignKey(User,db_column="reserved_by",null=True,blank=True,on_delete=models.DO_NOTHING)
    shelf_no = models.IntegerField(null=True,blank=True)
    author = models.CharField(max_length=100)
    clicks = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)