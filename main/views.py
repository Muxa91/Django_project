from django.shortcuts import render
from django.http import HttpResponse
from .forms import Userform
from . import models
import os
def index(request):
    return render(request, "main/index.html")

def other_page(request):
    return render(request, "main/other.html")

def works(request):
    return render(request, "main/works.html")

def images(request):
    works = ""
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    files = '{}/static/images/works/'.format(cur_dir)
    filelist= os.listdir(files)
    for file in filelist:
        works += '<div style=\'margin:5px;display: inline;\' class="' + str(file) + '" >' \
                '<a href=\'static/images/works/' + str(file) +'\'>' \
                '<img style=\'width: 300px; cursor: pointer; border: 1px solid #FFF;animation: rotate 1s;\' src=\'static/images/works/' \
                 + str(file) + '\' alt=\'' + str(file) + '\'> </a></div>'
    return HttpResponse(works)

def autorization(request):
    userform = Userform(request.POST or None)
    if request.method == 'POST':
        if userform.is_valid():
            name = request.POST.get('name')
            age  = request.POST.get('age')
            email  = request.POST.get("email")
            models.migrate(name, age)


            return HttpResponse("<h2>Hello, {0} age {1} </h2>".format(name, age))

        else:
            return render(request, "main/index.html/", {"form": userform})
    else:
        return render(request, "main/index.html/", {"form":userform})