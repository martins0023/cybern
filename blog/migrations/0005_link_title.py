# Generated by Django 4.0.2 on 2022-04-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
