from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^submit/(?P<id>\d+)$', views.submit),
    url(r'^delete/(?P<id>\d+)$', views.delete)
    # url(r'^newWord$', views.newWord),
    # url(r'^reset$', views.reset),
    # url(r'^newWord$', views.newWord)     # This line has changed!
]
