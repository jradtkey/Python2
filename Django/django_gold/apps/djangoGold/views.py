from __future__ import unicode_literals
from random import randint
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime

def index(request):
    return render(request, 'djangoGold/index.html')

def process_farm(request):
    if request.method == 'POST':
        if 'gold' not in request.session:
            add = randint(10,20)
            request.session['gold'] = add
            word = "You earned", add
        else:
            add = randint(10,20)
            request.session['gold'] += add
            word = "You earned", add

    else:
        print "hi"

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    temp_list = request.session['activities']
    temp_list.append(word)
    request.session['activities'] = temp_list

    return redirect('/')

def process_cave(request):
    if request.method == 'POST':
        if 'gold' not in request.session:
            add = randint(4,10)
            request.session['gold'] = add
            word = "You earned", add

        else:
            add = randint(4,10)
            request.session['gold'] += add
            word = "You earned", add

    else:
        print "hi"

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    temp_list = request.session['activities']
    temp_list.append(word)
    request.session['activities'] = temp_list

    return redirect('/')

def process_house(request):
    if request.method == 'POST':
        if 'gold' not in request.session:
            add = randint(1,5)
            request.session['gold'] = add
            word = "You earned", add

        else:
            add = randint(1,5)
            request.session['gold'] += add
            word = "You earned", add

    else:
        print "hi"

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    temp_list = request.session['activities']
    temp_list.append(word)
    request.session['activities'] = temp_list

    return redirect('/')

def process_casino(request):
    if request.method == 'POST':
        rand = randint(0,1)
        if rand == 1:
            if 'gold' not in request.session:
                add = random.randint(0,50)
                request.session['gold'] = add
                word = "You earned", add

            else:
                print rand
                add = randint(0,50)
                request.session['gold'] += add
                word = "You earned", add

        else:
            if 'gold' not in request.session:
                subtract = random.randint(0,50)
                request.session['gold'] = 0 - add
                word = "You lost", add

            else:
                print rand
                add = randint(0,50)
                request.session['gold'] -= add
                word = "You lost", add
    else:
        print "hi"

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    temp_list = request.session['activities']
    temp_list.append(word)
    request.session['activities'] = temp_list

    return redirect('/')

def clear(request):
    if request.method == 'POST':
        request.session['gold'] = 0
        request.session['activities'] = []
        return redirect('/')
