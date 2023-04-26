from xml.parsers.expat import model
from django.contrib import admin
from . models import CustomUser

admin.site.register(CustomUser)