# Generated by Django 2.1.1 on 2018-11-26 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181126_0552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='Personid',
        ),
    ]
