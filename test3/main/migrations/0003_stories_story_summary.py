# Generated by Django 2.1.5 on 2020-11-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201111_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='story_summary',
            field=models.CharField(default='', max_length=200),
        ),
    ]