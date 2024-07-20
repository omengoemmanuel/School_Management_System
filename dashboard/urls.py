from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('userprofile', views.userprofile),
    path('clearance', views.clearance),
    path('fees', views.fees),
    path('onlinereporting', views.onlinereporting),
    path('unitregistration', views.unitregistration),
    path('examcard', views.examcard),
    path('myassignment', views.myassignment)

]
