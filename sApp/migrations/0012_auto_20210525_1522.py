# Generated by Django 3.2.3 on 2021-05-25 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sApp', '0011_udata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='udata',
            old_name='performer_name',
            new_name='eventAttendanceMode',
        ),
        migrations.RemoveField(
            model_name='udata',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='udata',
            name='startDate',
        ),
    ]
