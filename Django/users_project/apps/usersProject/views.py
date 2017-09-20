from __future__ import unicode_literals
import random, string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime

def index(request):
    return render(request, 'usersProject/index.html')
