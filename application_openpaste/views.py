from django.shortcuts import render
from application_openpaste.models import *
# Create your views here.

def start_page(request):

    return render(request, 'start_page.html', {
    })

def all_inset(request):

    return render(request, 'all_inset.html', {
    })

def show_one_inset(request):

    return render(request, 'show_one_inset.html', {
    })