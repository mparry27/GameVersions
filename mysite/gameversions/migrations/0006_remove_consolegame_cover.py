# Generated by Django 2.2 on 2020-12-09 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameversions', '0005_consolegame_recommended_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consolegame',
            name='cover',
        ),
    ]
