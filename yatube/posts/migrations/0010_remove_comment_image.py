# Generated by Django 2.2.16 on 2022-12-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
