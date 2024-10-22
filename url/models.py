from __future__ import unicode_literals
from url_normalize import url_normalize

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.core.exceptions import ValidationError

from django.utils.crypto import get_random_string
# Create your models here.

class Url(models.Model):

    old_url = models.CharField(verbose_name='URL original',help_text='Digite a URL a ser encurtada.',blank=False,null=False,max_length=100)
    new_url = models.CharField(verbose_name='Codigo da URL encurtada.',default='',max_length=700,editable = False)
    clicked = models.IntegerField(default=0)

    def __str__(self):
        return self.old_url
    
    def concatenateUrl(self):
        return '127.0.0.1:8000/' + self.new_url
    
    def save(self,*args,**kwargs):
        self.new_url = get_random_string(length=5, allowed_chars='abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789')
        if not self.id:
            if self.old_url.startswith('https://www.'):
                self.old_url = self.old_url.replace('https://www.', '', 1)
            elif self.old_url.startswith('http://www.'):
                self.old_url = self.old_url.replace('http://www.', '', 1)
            elif self.old_url.startswith('https://'):
                self.old_url = self.old_url.replace('https://', '', 1)
            elif self.old_url.startswith('http://'):
                self.old_url = self.old_url.replace('http://', '', 1)

        
                
        
        super(Url, self).save(*args, **kwargs)


    def clean(self):
        if not self.id:
            if self.old_url.startswith('https://www.'):
                self.old_url = self.old_url.replace('https://www.', '', 1)
            elif self.old_url.startswith('http://www.'):
                self.old_url = self.old_url.replace('http://www.', '', 1)
            elif self.old_url.startswith('https://'):
                self.old_url = self.old_url.replace('https://', '', 1)
            elif self.old_url.startswith('http://'):
                self.old_url = self.old_url.replace('http://', '', 1)

            if Url.objects.filter(old_url = self.old_url):
                print(Url.objects.filter(old_url = self.old_url))
                print(self.old_url)
                raise ValidationError('Link ja cadastrado!!')
            else:
                pass
            
