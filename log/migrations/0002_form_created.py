# Generated by Django 3.0.1 on 2020-01-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
