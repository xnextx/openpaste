#-*-coding:utf-8-*-
from django.shortcuts import render
from application_openpaste.models import *
import re
# Create your views here.

# Tools

def show_one_inset_tool(request):
    url = request.get_full_path()
    priv = re.search('-.*-', url).group()

    if(priv[1] == '1'):#Prywatny
        inset = ""
        for x in Inset.objects.filter(url_private=url[15:]):
            inset += x.content + ", "
        return inset

    elif(priv[1] == '0'):#Publiczny
        inset = ""
        for x in Inset.objects.filter(id=url[15:]):
           inset += u'''Autor: %s <br/> <textarea style="color:black">Treść: %s </textarea><br/>''' % (x.owner, x.content)
        return inset

    else:
        return False
# End Tools

def start_page(request):

    return render(request, 'start_page.html', {

    })

def all_inset(request):

    return render(request, 'all_inset.html', {

    })

def show_one_inset(request):

    return render(request, 'show_one_inset.html', {
        'show_inset' : show_one_inset_tool(request),
    })