# Generated by Django 3.2.23 on 2023-11-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.CharField(default='Type your Message', max_length=1000),
        ),
    ]