# Generated by Django 2.1.5 on 2020-12-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_telling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telling',
            name='content',
            field=models.TextField(),
        ),
    ]