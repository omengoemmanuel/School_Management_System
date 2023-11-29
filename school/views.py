from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import messagess, gallery, staffs

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .form import CreateUserForm
from django.contrib import messages

from django.http import request
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student')

        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'login.html')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginpage')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginpage')

    context = {'form': form}
    return render(request, 'register.html', context)


def staff(request):
    slides = staffs.objects.all()
    return render(request, 'staff.html', {'navbar': 'staffs', 'slides': slides})


def news(request):
    return render(request, 'news.html')


def galleryy(request):
    slidess = gallery.objects.all()

    return render(request, 'gallery.html', {'navbar': 'galleryy', 'slidess': slidess})


def element(request):
    return render(request, 'elements.html')


def enroll(request):
    return render(request, 'enroll.html')


def messageinsert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if len(request.FILES) != 0:
            image = request.FILES['image']
        query = messagess(name=name, email=email, subject=subject, message=message, image=image)
        query.save()

    return redirect("/contact")


@login_required(login_url='loginpage')
def student(request):
    return render(request, 'student.html')

# class SignUp(CreateView):
#   model = CustomUser
#  form_class = CustomUserCreationForm
# success_url = reverse_lazy('school.login')
# template_name = 'register.html'


# class UserLogin(LoginView):
#   template_name = 'login.html'
