from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# Create your views here.

def firstview(request):
    return HttpResponse('Hello World')


def register_student(request):
    return render(request, 'register_student.html')
