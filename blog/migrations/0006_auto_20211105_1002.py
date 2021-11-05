# Generated by Django 3.2.8 on 2021-11-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(default='Foto'),
        ),
    ]