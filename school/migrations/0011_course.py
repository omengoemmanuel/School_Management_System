# Generated by Django 3.2.23 on 2023-11-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bronchure', models.FileField(upload_to='upload/pdfs')),
            ],
        ),
    ]
