# Generated by Django 4.1 on 2022-08-26 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_form_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='CXstatus',
            new_name='CX_status',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='crewStatus',
            new_name='crew_status',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='dailyProgress',
            new_name='daily_progress',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='nextDayPlan',
            new_name='next_day_plan',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='siteID',
            new_name='site_ID',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='currDay',
            new_name='work_date',
        ),
    ]