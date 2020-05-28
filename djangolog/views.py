from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('hi kia mohammadi kani savaran')
    return render(request , 'Home.html')

def about(request):
    # return HttpResponse('Home')
    return render(request , 'about.html')
