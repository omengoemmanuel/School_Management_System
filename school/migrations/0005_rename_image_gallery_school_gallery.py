# Generated by Django 3.2.23 on 2023-11-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='image',
            new_name='school_gallery',
        ),
    ]
