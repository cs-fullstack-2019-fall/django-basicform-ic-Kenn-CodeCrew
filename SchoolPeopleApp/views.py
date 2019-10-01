from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Test URL")

def test(request):
    return render(request, "SchoolPeopleApp/index.html")

def gotForm(request):
    print(request.POST)
    return HttpResponse("Hello " + request.POST['textField'])