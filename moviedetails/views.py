from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Moviesdetail

# Create your views here.
def index(request):
    # return HttpResponse("Hi Welcome to Home Page")
    # templates = loader.get_template('home.html')
    # return HttpResponse(templates.render())

    # mymovies  =  Moviesdetail.objects.all().values()
    # output    = ""
    # for m in mymovies:
    #     output += m["Name"]
    #     return HttpResponse(output)
    mymovies  =  Moviesdetail.objects.all().values()
    templates = loader.get_template('index.html')
    data      = {
        'mymovies':mymovies,
    }
    return HttpResponse(templates.render(data, request))


