from django.shortcuts import render
from django.http import HttpResponse
from .models import School

# Create your views here.
def index(request):
    return HttpResponse("Test URL")

def test(request):
    return render(request, "SchoolPeopleApp/index.html")

def gotForm(request):
    schoolArray = School.objects.all()
    print(request.POST)
    context = {
        "myName": request.POST['textField'],
        "myPassword": request.POST['passwordField'],
        "schoolArray": schoolArray,
    }
    return render(request, 'SchoolPeopleApp/gotForm.html', context)

