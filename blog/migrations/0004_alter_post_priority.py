# Generated by Django 3.2.8 on 2021-10-31 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Nejvyšší'), (2, 'Vysoká'), (3, 'Střední'), (4, 'Nízká'), (5, 'Nejnižší')], default=3),
        ),
    ]
