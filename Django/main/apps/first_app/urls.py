from django.conf.urls import url, include
from django.contrib import admin
from . import views

print "I am urls"         # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/index', views.blogs),     # This line has changed!
    url(r'^blogs/new', views.new),
    url(r'^blogs/(?P<number>\d+)$', views.show),
    url(r'^blogs/(?P<number>\d+)/edit', views.edit),
    url(r'^blogs/(?P<number>\d+)/delete', views.destroy),
    url(r'^surveys/', views.surveys),
    url(r'^surveys/new', views.newSurveys),
    url(r'^register/', views.register),
    url(r'^login/', views.smelly),
    url(r'^blogs/create', views.create)
]
