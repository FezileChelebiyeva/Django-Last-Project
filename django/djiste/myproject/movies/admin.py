from django.contrib import admin
from .models import *
# Register your models here.
 
# admin.site.register(Movies)
models = (Movies, Contacts)

for m in models:
   admin.site.register(m)
