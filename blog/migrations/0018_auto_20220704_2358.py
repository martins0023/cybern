# Generated by Django 2.2.14 on 2022-07-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20220704_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(max_length=2000),
        ),
    ]
