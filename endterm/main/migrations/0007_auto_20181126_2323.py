# Generated by Django 2.1.1 on 2018-11-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_achievements_personid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='Categoryid',
        ),
        migrations.AddField(
            model_name='achievements',
            name='Person',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Person'),
        ),
    ]
