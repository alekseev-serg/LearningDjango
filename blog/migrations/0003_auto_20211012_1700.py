# Generated by Django 3.2.7 on 2021-10-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210929_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]