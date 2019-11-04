from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')

def experience(request):
    return render(request, 'first_exp.html')

def second_experience(request):
    return render(request, 'second_exp.html')

def third_experience(request):
    return render(request, 'third_exp.html')

def education(request):
    return render(request, 'education.html')

def skills(request):
    return render(request, 'skills.html')

# Create your views here.

