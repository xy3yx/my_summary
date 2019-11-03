from django.shortcuts import render

def index(request):
    return render(request, 'MySummary/homepage.html', )

# Create your views here.
