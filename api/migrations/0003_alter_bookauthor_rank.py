# Generated by Django 4.1.6 on 2023-02-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_author_options_alter_bookauthor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='rank',
            field=models.PositiveIntegerField(),
        ),
    ]
