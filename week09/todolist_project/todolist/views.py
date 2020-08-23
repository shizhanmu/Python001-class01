from django.shortcuts import HttpResponse, render

def loadme(request):
    return HttpResponse("Hello, world!")
