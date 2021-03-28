# Generated by Django 3.1.6 on 2021-03-28 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_auto_20210328_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reservation_id',
            field=models.OneToOneField(blank=True, db_column='reservation_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian.reservation'),
        ),
    ]
