# Generated by Django 3.2.7 on 2021-10-12 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_rename_comlete_task_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
