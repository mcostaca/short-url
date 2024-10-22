from django.shortcuts import render
from .models import Url
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def retriving_url(request, url):
    url_find = get_object_or_404(Url,new_url = url)
    if url_find:
        url_find.clicked += 1
        url_find.save(update_fields=['clicked'])
    
    return redirect('https://www.' + url_find.old_url)