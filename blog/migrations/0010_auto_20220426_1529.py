# Generated by Django 4.0.2 on 2022-04-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(max_length=100),
        ),
    ]
