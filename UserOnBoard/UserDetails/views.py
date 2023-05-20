from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

from .models import UserAddress, UserDetails
from .pagination import Paginationno
from .serializer import AddressSerializer, UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# class UserDetail(generics.RetrieveUpdateAPIView):
class UserDetails(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserDetails.objects.all()

    # For Authontication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    #For Pagination
    pagination_class = Paginationno
    #For filteration
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']
    @action(detail=False, methods=['get'])
    def get_address(self, request):
        objs = UserAddress.objects.all()
        serializer = AddressSerializer(objs, many=True)
        return Response({
            'status': True,
            'message': 'data fetched',
            'data': serializer.data
        })

    @action(detail=False, methods=['post'])
    def add_address(self, request):
        try:
            data = request.data
            serializer = AddressSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'succeed data',
                    'data': serializer.data
                })
            return Response({
                'status': True,
                'message': 'Invalid data'

            })

        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Invalid data'
        })


# class AddressDetail(viewsets.ModelViewSet):
#     serializer_class = AddressSerializer
#     queryset = UserAddress.objects.all()

## In Diffrent manner_ Not used Serializer
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
