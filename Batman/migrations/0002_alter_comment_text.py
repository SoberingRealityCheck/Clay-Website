# Generated by Django 5.0.6 on 2024-07-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Batman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=255),
        ),
    ]
