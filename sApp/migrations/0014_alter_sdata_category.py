# Generated by Django 3.2.3 on 2021-05-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sApp', '0013_alter_sdata_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdata',
            name='category',
            field=models.TextField(blank=True, default='Noting', null=True),
        ),
    ]
