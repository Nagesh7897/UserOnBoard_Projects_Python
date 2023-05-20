from django.core import validators
from django.db import transaction

from UserDetails.models import UserDetails, UserAddress
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validators.EmailValidator()])
    class Meta:
        model = UserDetails
        #fields = ['uid', 'first_name', 'email']
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
   # user = UserSerializer()

    class Meta:
        model = UserAddress
       # fields = ['uid', 'address', 'country', 'userDetails']
        fields = '__all__'
    #
    # @transaction.atomic
    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = UserDetails.objects.create(**user_data)
    #     address = UserAddress.objects.create(user=user, **validated_data)
    #     return address
    #
    # @transaction.atomic
    # def update(self, instance, validated_data):
    #     UserDetails_data = validated_data.pop('user')
    #     user = instance.UserDetails
    #     user.first_name = UserDetails_data.get('first_name', user.first_name)
    #     user.email = UserDetails_data.get('email', user.email)
    #     user.save()
    #
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.save()
    #     return instance
