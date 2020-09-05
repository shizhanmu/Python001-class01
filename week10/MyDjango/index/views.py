from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello Django!")
    return redirect("ranking")
