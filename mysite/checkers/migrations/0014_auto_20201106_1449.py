# Generated by Django 3.1.1 on 2020-11-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkers', '0013_auto_20201106_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_session',
            name='game_id',
            field=models.CharField(max_length=255),
        ),
    ]
