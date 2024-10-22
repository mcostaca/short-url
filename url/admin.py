# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Url
from django.utils.html import escape, mark_safe
# Register your models here.


class UrlAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'
    def concatenateUrl(self):
        return '127.0.0.1:8000/' + self.new_url
    
    concatenateUrl.short_description = 'LINK ENCURTADO'
    
    def qrCodeGen(self):
        url = self.concatenateUrl()
        return mark_safe('<img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={url}" width="296" height="296" alt="QR Code"/>'.format(url=url))

    
    
    qrCodeGen.allow_tags = True
    qrCodeGen.short_description = 'QR CODE'

    list_display = ['old_url',concatenateUrl, qrCodeGen]

    def concatenateUrl(self):
        '127.0.0.1:8000/' + self.new_url

    fields =('old_url','new_url',)

    

    def get_readonly_fields(self, request, obj=None):
        

        if obj:
            return self.readonly_fields + ('new_url','old_url',)
        else:
            return self.readonly_fields + ('new_url',)
    
    


#admin_site.register(Url, UrlAdmin)
admin.site.register(Url,UrlAdmin)