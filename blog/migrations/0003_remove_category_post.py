# Generated by Django 3.2.8 on 2021-10-27 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
    ]