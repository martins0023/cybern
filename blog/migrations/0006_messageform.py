# Generated by Django 4.0.2 on 2022-04-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_link_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='Message is required')),
            ],
        ),
    ]
