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


class enroll(models.Model):
    firstname = models.CharField(max_length=50, blank=False, null=False)
    mail = models.EmailField(blank=False, null=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    pno = models.IntegerField(null=False, blank=False)
    nid = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=6, blank=False, null=False)
    yoe = models.IntegerField(blank=False, null=False)
    course_cate = models.CharField(max_length=150, null=False, blank=False)
    t_course = models.CharField(max_length=100, null=False, blank=False)
    up_birth = models.FileField(upload_to="upload/enrolls", default="upload/enroll/birth.pdf")
    up_id = models.FileField(upload_to="upload/enrolls", default="upload/enroll/id.pdf")
    up_kcse = models.FileField(upload_to="upload/enrolls", default="upload/enroll/kcse.pdf")

    def __str__(self):
        return self.firstname


class testimonial(models.Model):
    message = models.CharField(max_length=300, blank=False, null=False)
    photo = models.ImageField(upload_to="upload/testimonials", default="upload/testimonial/photo.jpg")
    name = models.CharField(max_length=30, blank=False, null=False)
    position = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class ourteam(models.Model):
    photo = models.ImageField(upload_to="upload/our team", default="upload/our team/team.png")
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.name

# class CustomUser(AbstractUser):
# f_name = models.CharField(max_length=20, blank=False, null=False)
# m_name = models.CharField(max_length=20, blank=False, null=False)
# dep = models.CharField(max_length=20, blank=False, null=False)
# hcounty = models.CharField(max_length=20, blank=False, null=False)
# hscounty = models.CharField(max_length=30, blank=False, null=False)
# id_no = models.PositiveIntegerField(blank=False, null=False)
# regno = models.CharField(max_length=20, blank=False, null=False)
# phone = models.PositiveIntegerField(blank=False, null=False)
