from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def explore(request):
    return render(request, 'explore.html')

def object_detection(request):
    return render(request, 'object.html')

def weather(request):
    return render(request, 'weather.html')


