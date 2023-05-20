
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from UserDetails.views import UserDetails

#
# urlpatterns = [
#     path('UserDetail/<str:new_uuid>/', UserDetail.as_view(), name='UserDetails'),
# ]
router = routers.DefaultRouter()
router.register(r'userdetails', UserDetails, basename='UserDetails')
# router.register(r'AddressDetails', AddressDetails, basename='AddressDetails')

urlpatterns = [
    path('', include(router.urls)),
]