from tkinter.messagebox import RETRY
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'webapp/home.html')

def about(request):
    return render(request, 'webapp/about.html')

def contacto(request):
    return render(request, 'webapp/contact.html')