# Generated by Django 4.1 on 2022-08-11 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='user',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
