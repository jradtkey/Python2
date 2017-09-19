from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'showTime/page.html', context)

def showTime(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'showTime/index.html', context)
