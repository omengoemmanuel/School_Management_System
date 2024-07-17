# Generated by Django 3.2.24 on 2024-07-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0028_ourteam_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='enroll1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namee', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('idno', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('yoe', models.CharField(max_length=4)),
                ('category', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('id_no', models.FileField(default='upload/enrolls/id.pdf', upload_to='upload/enrolls')),
                ('kcse', models.FileField(default='upload/enrolls/kcse.pdf', upload_to='upload/enrolls')),
            ],
        ),
    ]