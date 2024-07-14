from django.contrib import admin

from .models import messagess, gallery, staffs, enroll, testimonial

from django.contrib.auth.admin import UserAdmin
#from school.form import CustomUserCreationForm, CustomUserChangeForm

#from school.models import CustomUser

# Register your models here.
admin.site.register(messagess)
admin.site.register(gallery)
admin.site.register(staffs)
admin.site.register(enroll)
admin.site.register(testimonial)
#admin.site.register(CustomUser)

#admin.site.register(CustomUserAdmin)

#class CustomUserAdmin(UserAdmin):
   # add_form = CustomUserCreationForm
    #form = CustomUserChangeForm


