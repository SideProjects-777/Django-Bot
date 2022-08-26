# Generated by Django 4.1 on 2022-08-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currDay', models.DateField(auto_now=True)),
                ('crewStatus', models.CharField(choices=[('WORK', 'At work'), ('OFF', 'Day off'), ('VACATION', 'Vacation')], default='WORK', max_length=9)),
                ('siteID', models.TextField(max_length=10)),
                ('CXstatus', models.CharField(choices=[('CXS', 'CXS'), ('PROGRESS', 'In progress'), ('HOLD', 'On hold '), ('CXC', 'CXC')], default='CXS', max_length=9)),
                ('completeness', models.TextField(max_length=100)),
                ('dailyProgress', models.TextField(max_length=250)),
                ('nextDayPlan', models.TextField(max_length=250)),
                ('notes', models.TextField(max_length=250)),
                ('market', models.TextField(max_length=250)),
            ],
        ),
    ]
