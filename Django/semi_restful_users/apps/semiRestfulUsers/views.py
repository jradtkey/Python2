from __future__ import unicode_literals
import random, string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from models import *
from django.contrib import messages

def index(request):

    context = {
        "users": User.objects.all()
    }

    return render(request,'semiRestfulUsers/index.html', context)

def add(request):
    return render(request,'semiRestfulUsers/newUser.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add')
    else:
        User.objects.create(full_name = request.POST['full_name'], email = request.POST['email'])
        return redirect('/')

def show(request, id):
    context = {
        "users": User.objects.get(id=id)
    }
    return render(request,'semiRestfulUsers/show.html', context)

def edit(request, id):
    context = {
        "users": User.objects.get(id=id)
    }
    return render(request,'semiRestfulUsers/edit.html', context)

def submit(request, id):
    b = User.objects.get(id=id)
    b.full_name = request.POST['full_name']
    b.save()

    a = User.objects.get(id=id)
    a.email = request.POST['email']
    a.save()

    return redirect('/')

def delete(request, id):
    b = User.objects.get(id=id)
    b.delete()
    return redirect('/')
