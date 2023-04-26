from django.contrib import admin
from . models import CustomUser
# Register your models here.



@admin.register(CustomUser)
class userAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "email"]


# admin.site.register(CustomUser)