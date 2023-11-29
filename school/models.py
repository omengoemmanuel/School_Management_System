from django.db import models
from django.contrib.auth.models import AbstractUser


class messagess(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=300, blank=False)
    message = models.CharField(max_length=1000, blank=False, default="Type your Message", null=True)
    image = models.ImageField(upload_to="upload/pdfs", blank=False)

    def __str__(self):
        return self.name


class gallery(models.Model):
    photo = models.ImageField(upload_to="upload/gallery", default="upload/gallery/profile.jpg")


class staffs(models.Model):
    name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="upload/staff", )

    def __str__(self):
        return self.name


#class CustomUser(AbstractUser):
   # f_name = models.CharField(max_length=20, blank=False, null=False)
    #m_name = models.CharField(max_length=20, blank=False, null=False)
    #dep = models.CharField(max_length=20, blank=False, null=False)
    #hcounty = models.CharField(max_length=20, blank=False, null=False)
    #hscounty = models.CharField(max_length=30, blank=False, null=False)
    #id_no = models.PositiveIntegerField(blank=False, null=False)
    #regno = models.CharField(max_length=20, blank=False, null=False)
    #phone = models.PositiveIntegerField(blank=False, null=False)
