# Generated by Django 4.1 on 2022-09-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200)),
                ('tg_chat', models.CharField(max_length=200)),
                ('tg_message', models.CharField(max_length=100)),
            ],
        ),
    ]
