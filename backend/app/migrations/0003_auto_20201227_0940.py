# Generated by Django 3.1.4 on 2020-12-27 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201227_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
