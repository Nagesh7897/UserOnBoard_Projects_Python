from django.contrib import admin
from .models import UserDetails, UserAddress

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(UserAddress)