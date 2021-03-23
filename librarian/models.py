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

class SmallCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(SmallCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class book_category(models.Model):
    category = SmallCharField(max_length=100,unique=True)


class reservation(models.Model):
    reserved_at = models.DateTimeField(auto_now_add=True)
    reserved_by = models.ForeignKey(User,db_column="reserved_by",on_delete=models.CASCADE)

class book(models.Model):
    description = models.TextField()
    cover_pic = models.ImageField(upload_to=path_and_rename)
    title = SmallCharField(max_length=100)
    category_id = models.ForeignKey(book_category,db_column="category_id", on_delete=models.CASCADE)
    reservation_id = models.ForeignKey(reservation,db_column="reservation_id",null=True,blank=True,on_delete=models.SET_NULL)
    shelf_no = models.IntegerField()
    asin_no = SmallCharField(max_length=100)
    author = SmallCharField(max_length=100)
    clicks = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)