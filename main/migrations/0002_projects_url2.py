# Generated by Django 4.2.7 on 2024-02-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='url2',
            field=models.URLField(blank=True),
        ),
    ]
