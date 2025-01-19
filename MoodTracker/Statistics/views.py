from django.shortcuts import render

def graph(request):
    return render(request, 'graph.html')

def calendar(request):  
    return render(request, 'calendar.html')
