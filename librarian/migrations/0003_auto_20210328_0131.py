# Generated by Django 3.1.6 on 2021-03-27 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('librarian', '0002_auto_20210328_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latest_visited_book',
            name='firstbook',
            field=models.ForeignKey(blank=True, db_column='firstbook', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='firstbook', to='librarian.book'),
        ),
        migrations.AlterField(
            model_name='latest_visited_book',
            name='secondbook',
            field=models.ForeignKey(blank=True, db_column='secondbook', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondbook', to='librarian.book'),
        ),
        migrations.AlterField(
            model_name='latest_visited_book',
            name='user',
            field=models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
