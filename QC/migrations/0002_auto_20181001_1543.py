# Generated by Django 2.1.1 on 2018-10-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QC', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='media_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='media_type',
            new_name='mime_type',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='media_url',
            new_name='file',
        ),
    ]
