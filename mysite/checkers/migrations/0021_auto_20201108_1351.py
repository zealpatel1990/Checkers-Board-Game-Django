# Generated by Django 3.1.1 on 2020-11-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkers', '0020_game_session_is_open_to_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_session',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
