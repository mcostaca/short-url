from django.conf.urls import url, include
from django.contrib import admin
from url.views import retriving_url

urlpatterns = [
    url(r'^(?P<url>[\w-]+)/$',retriving_url),
]