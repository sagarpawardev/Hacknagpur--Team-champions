# Generated by Django 3.1.4 on 2020-12-27 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]