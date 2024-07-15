# Generated by Django 3.2.24 on 2024-07-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0024_rename_first_name_enroll_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('photo', models.ImageField(default='upload/testimonial/photo.jpg', upload_to='upload/testimonials')),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=10)),
            ],
        ),
    ]