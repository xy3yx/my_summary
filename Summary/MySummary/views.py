from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')

def experience(request):
    return render(request, 'first_exp.html')

def second_experience(request):
    return render(request, 'second_exp.html')

def third_experience(request):
    return render(request, 'third_exp.html')

# Create your views here.

