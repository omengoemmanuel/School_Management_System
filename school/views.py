from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import messagess, gallery, staffs
from .models import enroll, testimonial, ourteam, enroll1

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
    testi = testimonial.objects.all()
    return render(request, 'index.html', {'navbar': 'home', 'testi': testi})


def about(request):
    team = ourteam.objects.all()
    return render(request, 'about.html', {'navbar': 'about', 'team': team})


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


def enrollsinsert(request):
    if request.method == "POST":
        namee = request.POST.get('namee')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        idno = request.POST.get('idno')
        gender = request.POST.get('gender')
        yoe = request.POST.get('yoe')
        category = request.POST.get('category')
        course = request.POST.get('course')
        upid = request.FILES['upid']
        kcse = request.FILES['kcse']

        print(f"Received data: {namee}, {email}, {address}, {phone}, {idno}, {gender}, {yoe}, {category}, {course}")

        query5 = enroll1(namee=namee, email=email, address=address, phone=phone, idno=idno, gender=gender, yoe=yoe,
                         category=category, course=course, upid=upid, kcse=kcse)

        query5.save()
        return redirect("/enroll1")
    return redirect("/enroll1")


def enrollinsert(request):
    if request.method == "POST":
        first_name1 = request.POST.get('firstname')
        mail = request.POST.get('mail')
        address = request.POST.get('address')
        pno = request.POST.get('pno')
        nid = request.POST.get('nid')
        gender = request.POST.get('gender')
        yoe = request.POST.get('yoe')
        course_cate = request.POST.get('coursecate')
        t_course = request.POST.get('tcourse')

        if len(request.FILES) != 0:
            up_birth = request.FILES['upbirth']
            up_id = request.FILES['upid']
            up_kcse = request.FILES['upkcse']

            query1 = enroll(firstname=first_name1, mail=mail, address=address, pno=pno, nid=nid, gender=gender, yoe=yoe,
                            course_cate=course_cate, t_course=t_course, up_id=up_id, up_birth=up_birth, up_kcse=up_kcse)
            query1.save()

        return redirect("/enroll")

    return redirect("/enroll")


@login_required(login_url='loginpage')
def student(request):
    return render(request, 'student.html')


def enroll(request):
    return render(request, 'enroll.html')


def enroll1(request):
    return render(request, 'enroll1.html')


def dashboard(request):
    return render(request, 'dashboard.html')

# class SignUp(CreateView):
#   model = CustomUser
#  form_class = CustomUserCreationForm
# success_url = reverse_lazy('school.login')
# template_name = 'register.html'


# class UserLogin(LoginView):
#   template_name = 'login.html'
