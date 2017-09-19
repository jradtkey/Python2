"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.first_app.urls')),
    url(r'^blogs/index', include('apps.first_app.urls')),
    url(r'^blogs/new', include('apps.first_app.urls')),
    url(r'^blogs/create', include('apps.first_app.urls')),
    url(r'^blogs/{{number}}', include('apps.first_app.urls')),
    url(r'^blogs/{{number}}/edit', include('apps.first_app.urls')),
    url(r'^blogs/{{number}}/delete', include('apps.first_app.urls')),
    url(r'^surveys/', include('apps.first_app.urls')),
    url(r'^surveys/new', include('apps.first_app.urls')),
    url(r'^register/', include('apps.first_app.urls')),
    url(r'^login/', include('apps.first_app.urls'))   
]
