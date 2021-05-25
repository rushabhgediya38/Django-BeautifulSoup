from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(sData)
admin.site.register(InterestingUrl)
admin.site.register(Non_interesting_url)
