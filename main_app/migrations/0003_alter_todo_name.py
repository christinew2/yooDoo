# Generated by Django 3.2.6 on 2021-08-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]