# Generated by Django 2.2 on 2020-12-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameversions', '0004_game_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='consolegame',
            name='recommended_version',
            field=models.BooleanField(default=False),
        ),
    ]