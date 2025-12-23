from django.shortcuts import render
from . models import Create_User
from . serializers import  Create_User_serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class Create_Users(GenericAPIView,CreateModelMixin):
    querset=Create_User.objects.all()
    serializer_class=Create_User_serializer
    def post(self,request,*args,**kwargs):
        print("api is hiting")
        email=request.data.get('email')
        phone_number=request.data.get('phone_number')
        print(email)
        print(phone_number)
        if Create_User.objects.filter(email=email).exists():
            return Response({'error':'User with this mail already exists  '},status=status.HTTP_400_BAD_REQUEST)
        elif Create_User.objects.filter(phone_number=phone_number).exists():
            return Response({'error':'User with this mail already exists  '},status=status.HTTP_400_BAD_REQUEST)
        else:
            response=self.create(request,*args,**kwargs)
            if response.status_code==status.HTTP_201_CREATED:
                return Response({'message':'User Create Successfully '},status=status.HTTP_201_CREATED)
            return response
