# Generated by Django 3.2.8 on 2023-09-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
