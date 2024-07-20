from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def userprofile(request):
    return render(request, 'user.html')


def clearance(request):
    return render(request, 'clearance.html')


def fees(request):
    return render(request, 'fees.html')


def onlinereporting(request):
    return render(request, 'onlinereporting.html')


def unitregistration(request):
    return render(request, 'unitregistration.html')


def examcard(request):
    return render(request, 'examcard.html')


def myassignment(request):
    return render(request, 'myassignment.html')
