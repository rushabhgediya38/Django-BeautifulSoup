# Generated by Django 3.2.3 on 2021-05-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sApp', '0010_auto_20210525_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='uData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('startDate', models.DateTimeField(blank=True, null=True)),
                ('endDate', models.DateTimeField(blank=True, null=True)),
                ('performer_name', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(blank=True, default='Noting', max_length=256, null=True)),
            ],
        ),
    ]