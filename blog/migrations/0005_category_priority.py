# Generated by Django 3.2.8 on 2021-10-31 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Nejvyšší'), (2, 'Vysoká'), (3, 'Střední'), (4, 'Nízká'), (5, 'Nejnižší')], default=3),
        ),
    ]