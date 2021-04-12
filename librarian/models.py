from django.db import models
from django.contrib.auth.models import User
import os
from students import model
from uuid import uuid4
from django.contrib.auth.models import User

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
    def __str__(self):
        return self.category


class reservation(models.Model):
    reserved_at = models.DateTimeField(auto_now_add=True)
    reserved_by = models.ForeignKey(User,db_column="reserved_by",on_delete=models.CASCADE)
    def __str__(self):
        return str(self.reserved_by.id)

class book(models.Model):
    description = models.TextField()
    cover_pic = models.ImageField(upload_to=path_and_rename)
    title = models.CharField(max_length=100)
    category_id = models.ForeignKey(book_category,db_column="category_id", on_delete=models.CASCADE)
    reservation_id = models.OneToOneField(reservation,db_column="reservation_id",null=True,blank=True,on_delete=models.SET_NULL)
    shelf_no = models.CharField(max_length=10,null=True,blank=True)
    asin_no = models.CharField(max_length=100,null=True,blank=True)
    author = models.CharField(max_length=100)
    clicks = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        model.add_data(self.id,self.title,self.description,self.category_id.id)
    
    def delete(self):
        id = self.id
        super(book, self).delete()
        model.delete_data(id)

class latest_visited_book(models.Model):
    user = models.OneToOneField(User, db_column="user", on_delete=models.CASCADE)
    book_1 = models.ForeignKey(book, db_column="book_1", null=True, blank=True, related_name="book_1", on_delete=models.SET_NULL)
    book_2 = models.ForeignKey(book, db_column="book_2", null=True, blank=True, related_name="book_2", on_delete=models.SET_NULL)
    book_3 = models.ForeignKey(book, db_column="book_3", null=True, blank=True, related_name="book_3", on_delete=models.SET_NULL)
    book_4 = models.ForeignKey(book, db_column="book_4", null=True, blank=True, related_name="book_4", on_delete=models.SET_NULL)
    book_5 = models.ForeignKey(book, db_column="book_5", null=True, blank=True, related_name="book_5", on_delete=models.SET_NULL)
    book_1_click = models.IntegerField(null=True,blank=True)
    book_2_click = models.IntegerField(null=True,blank=True)
    book_3_click = models.IntegerField(null=True,blank=True)
    book_4_click = models.IntegerField(null=True,blank=True)
    book_5_click = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.firstbook.title
