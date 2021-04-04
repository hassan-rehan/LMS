# Generated by Django 3.1.6 on 2021-04-04 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import librarian.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('cover_pic', models.ImageField(upload_to=librarian.models.path_and_rename)),
                ('title', models.CharField(max_length=100)),
                ('shelf_no', models.IntegerField(blank=True, null=True)),
                ('asin_no', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(max_length=100)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('clicks', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='book_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', librarian.models.SmallCharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_at', models.DateTimeField(auto_now_add=True)),
                ('reserved_by', models.ForeignKey(db_column='reserved_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='latest_visited_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_1', models.ForeignKey(blank=True, db_column='book_1', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_1', to='librarian.book')),
                ('book_2', models.ForeignKey(blank=True, db_column='book_2', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_2', to='librarian.book')),
                ('book_3', models.ForeignKey(blank=True, db_column='book_3', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_3', to='librarian.book')),
                ('book_4', models.ForeignKey(blank=True, db_column='book_4', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_4', to='librarian.book')),
                ('book_5', models.ForeignKey(blank=True, db_column='book_5', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_5', to='librarian.book')),
                ('user', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category_id',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='librarian.book_category'),
        ),
        migrations.AddField(
            model_name='book',
            name='reservation_id',
            field=models.OneToOneField(blank=True, db_column='reservation_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian.reservation'),
        ),
    ]
