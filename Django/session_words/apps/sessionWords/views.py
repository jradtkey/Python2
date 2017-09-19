from __future__ import unicode_literals
import random, string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime

def index(request):
    # try:
    #     request.session['word']
    #     request.session['color'
    #     request.session['time']
    # except KeyError:
    #     request.session['word'] = 'none'
    #     request.session['color'] = 'red'
    #     request.session['time'] = 'none'
    return render(request,'sessionWords/index.html')

def process(request):
    if request.method == 'POST':
        request.session['word'] += [request.POST['word'] + ' - added on ' + strftime("%H:%M %p %m-%d-%Y", gmtime())]
        request.session['color'] = request.POST['color']
        # request.session['time'] += [strftime("%H:%M %p %m-%d-%Y", gmtime())]
        # request.session['list'] += request.session['word']
        # request.session['different'] += request.session['color']
        print request.session['color']
        return redirect('/')
    else:
        return redirect('/')
