from __future__ import unicode_literals
import random, string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request,'word_generator/index.html')

def newWord(request):
    request.session['tries'] += 1
    request.session['word'] = get_random_string(5)
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')

# Create your views here.
