# Generated by Django 3.2.23 on 2023-12-11 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_rename_fname_enroll_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='firstname',
            new_name='first_name',
        ),
    ]