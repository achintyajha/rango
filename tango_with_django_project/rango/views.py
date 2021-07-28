from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # dictionary for template variables
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # dictionary for template variables
    context_dict = {'boldmessage': "Hello, this is the most useless page ever"}
    return render(request, 'rango/about.html', context=context_dict)
