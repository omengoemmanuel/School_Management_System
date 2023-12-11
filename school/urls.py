from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about),
    path('contact', views.contact),
    path('loginpage', views.loginpage, name="loginpage"),
    path('logout', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('staff', views.staff),
    path('news', views.news),
    path('gallery', views.galleryy),

    path('element', views.element),
    path('enroll', views.enroll),
    path('messageinsert', views.messageinsert, name="messageinsert"),
    path('student', views.student, name="student"),
    path('enroll', views.enroll, name="enroll"),
    path('enrollinsert', views.enrollinsert, name="enrollinsert")

]