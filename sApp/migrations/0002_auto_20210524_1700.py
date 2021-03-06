# Generated by Django 3.2.3 on 2021-05-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sdata',
            name='SITE_URL',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sdata',
            name='author',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='sdata',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sdata',
            name='modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sdata',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
