# Generated by Django 2.2.14 on 2022-07-04 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.CharField(default=django.db.models.deletion.CASCADE, max_length=2000),
        ),
    ]
