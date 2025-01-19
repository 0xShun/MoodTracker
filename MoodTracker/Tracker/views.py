from django.shortcuts import render

def index(request):
    return render(request, 'dashboard.html')


def log_mood(request):
    return render(request, 'logmood.html')