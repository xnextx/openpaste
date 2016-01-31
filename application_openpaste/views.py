from django.shortcuts import render
from application_openpaste.models import *
# Create your views here.

def start_page(request):

    return render(request, 'start_page.html', {
    })