# Generated by Django 4.1.6 on 2023-02-17 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_book_additional_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image',
        ),
    ]
