# Generated by Django 2.0.6 on 2019-04-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='Time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todolist',
            name='user',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
