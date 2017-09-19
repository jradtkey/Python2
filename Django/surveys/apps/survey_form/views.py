from __future__ import unicode_literals
import random, string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):

    try:
        request.session['tries']
        request.session['name']
        request.session['location']
        request.session['language']
        request.session['comments']
    except KeyError:
        request.session['name'] = 'none'
        request.session['tries'] = 0
        request.session['location'] = 'none'
        request.session['language'] = 'none'
        request.session['comments'] = 'none'

    return render(request,'survey_form/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['tries'] += 1
        return redirect('/result')
    else:
        return redirect('/result')

def result(request):
    return render(request,'survey_form/result.html')
