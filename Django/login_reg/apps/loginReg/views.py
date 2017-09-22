from __future__ import unicode_literals
import random, string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from models import *
from django.contrib import messages
from flask import Flask, flash

import bcrypt


def index(request):
    return render(request,'loginReg/index.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())

        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], password = password)

        request.session['user_id'] = user.id

        return redirect('/success')

def success(request):
    context = {
        "users": User.objects.get(id=request.session['user_id'])
    }

    

    return render(request, 'loginReg/success.html', context)

def login(request):
    # errors = User.objects.basic_validator(request.POST)
    users = User.objects.filter(email=request.POST['email'])
    errors = {}
    if len(users) > 0:
        context = {
            'users': User.objects.filter(email=request.POST['email'])
        }

        for user in users:
            password1 = user.password
            request.session['user_id'] = user.id

        password2 = request.POST['password']
        if bcrypt.checkpw(password2.encode('utf-8'), password1.encode('utf-8')):
            return redirect('/success')
        else:
            errors["email_valid"] =  "Password does not match our database."
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')

    else:
        errors["no_email"] =  "Cannot find email in our database."
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        return redirect('/')
