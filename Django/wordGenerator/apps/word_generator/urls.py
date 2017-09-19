from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newWord$', views.newWord),
    url(r'^reset$', views.reset),
    # url(r'^newWord$', views.newWord)     # This line has changed!
]
