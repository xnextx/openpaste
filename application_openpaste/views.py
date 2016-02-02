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
        inset = []
        for x in Inset.objects.filter(id=url[15:]):
            inset.append(x.owner);
            inset.append(x.content);
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
        'owner' : show_one_inset_tool(request)[0],
        'content' : show_one_inset_tool(request)[1],
    })