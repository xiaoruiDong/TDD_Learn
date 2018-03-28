from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    # use httpresponse
    # return HttpResponse('<html><title>To-Do lists</title>')

    # Otherwise we can use render, The first object is the request object,
    # the second is the templates name
    return render(request, 'home.html')
