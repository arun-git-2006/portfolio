from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')  

def skills(request):
    return render(request, 'portfolio/skills.html')