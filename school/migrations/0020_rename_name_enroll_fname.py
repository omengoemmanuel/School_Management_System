# Generated by Django 3.2.23 on 2023-12-07 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_rename_namee_enroll_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='name',
            new_name='fname',
        ),
    ]
