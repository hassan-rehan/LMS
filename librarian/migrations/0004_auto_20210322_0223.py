# Generated by Django 3.1.6 on 2021-03-21 21:23

from django.db import migrations
import librarian.models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_auto_20210322_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_category',
            name='category',
            field=librarian.models.CategoryField(max_length=100),
        ),
    ]
