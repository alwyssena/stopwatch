from django.shortcuts import render
from . models import Create_User
from . serializers import  Create_User_Serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import status
from rest_framework.response import Response
from . serializers import Login_User_Serializer
from .utils import get_tokens_for_user

from . serializers import Course_serializer
from . models import Courses_Model
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from . serializers import Syllabus_serializer
from . models import Syllabus_Model

from . serializers import Specialization_serializer
from . models import Specializations

# Create your views here.
class Create_Users(GenericAPIView,CreateModelMixin):
    querset=Create_User.objects.all()
    serializer_class=Create_User_Serializer
    def post(self,request,*args,**kwargs):
        print("api is hiting")
        email=request.data.get('email')
        phone_number=request.data.get('phone_number')
        print(email)
        print(phone_number)
        if Create_User.objects.filter(email=email).exists():
            return Response({'error':'User with this mail already exists  '},status=status.HTTP_400_BAD_REQUEST)
        elif Create_User.objects.filter(phone_number=phone_number).exists():
            return Response({'error':'User with this phone number already exists  '},status=status.HTTP_400_BAD_REQUEST)
        else:
            response=self.create(request,*args,**kwargs)
            if response.status_code==status.HTTP_201_CREATED:
                print(request.data.get('password'))
                return Response({'message':'User Create Successfully '},status=status.HTTP_201_CREATED)
            return response
        
# login 
        
class Login(GenericAPIView):
    serializer_class=Login_User_Serializer
    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            tokens=get_tokens_for_user(user)

            return Response({'public_id':user.public_id,
                             'first_name':user.first_name,
                             'last_name':user.last_name,
                             'email':user.email,
                             'password':user.password,
                             'is_superuser':user.is_superuser,
                             'token':tokens['access'],
                             'refresh':tokens['refresh']
                             },status=status.HTTP_200_OK)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
# add Course 

class AddCourse(GenericAPIView,CreateModelMixin):
    serializer_class=Course_serializer
    permission_classes=[IsAdminUser]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

#get courese
class Course_details(GenericAPIView,ListModelMixin):
    serializer_class=Course_serializer
    queryset=Courses_Model.objects.all()
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
#modifiy

class Course_modify(GenericAPIView,UpdateModelMixin):
    serializer_class=Course_serializer
    queryset=Courses_Model.objects.all()
    permission_classes=[IsAdminUser]
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
        
#delete 

class Course_delete(GenericAPIView,DestroyModelMixin):
    serializer_class=Course_serializer
    queryset=Courses_Model.objects.all()
    permission_classes=[IsAdminUser]
    def delete(self,request,*args,**kwargs):
         self.destroy(request,*args,**kwargs)
         return Response({'message':"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    
#adding syllabus

class AddSyllabus(GenericAPIView,CreateModelMixin):
    serializer_class=Syllabus_serializer
    permission_classes=[IsAdminUser]
    def post(self,request,*args,**kwargs):
        course_id=request.data.get('course_id')
        syllabus=request.data.get('syllabus')
        data=[
            {'course_name':course_id,
             'module':item.get('module'),
             'description':item.get('description')  
             }for item in syllabus
        ]
        serializer=self.get_serializer(data=data,many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message':'Syllabus added successfully'},status=status.HTTP_201_CREATED)
#modify syllabus
class SyllabusModify(GenericAPIView,UpdateModelMixin):
    serializer_class=Syllabus_serializer
    queryset=Syllabus_Model.objects.all()
    permission_classes=[IsAdminUser]
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

#delete syllabus
class SyllabusDelete(GenericAPIView,DestroyModelMixin):
    serializer_class=Syllabus_serializer
    queryset=Syllabus_Model.objects.all()
    permission_classes=[IsAdminUser]
    def delete(self,request,*args,**kwargs):
        self.destroy(request,*args,**kwargs)
        return Response({'message':"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)

# Specializations can be added here similarly
class AddSpecialization(GenericAPIView,CreateModelMixin):
    serializer_class=Specialization_serializer
    permission_classes=[IsAdminUser]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

#retive specialization can be implemented similarly
class Specialization_details(GenericAPIView,ListModelMixin):
    serializer_class=Specialization_serializer
    queryset=Specializations.objects.all()
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
#modify specialization
class Specialization_modify(GenericAPIView,UpdateModelMixin):
    serializer_class=Specialization_serializer
    queryset=Specializations.objects.all()
    permission_classes=[IsAdminUser]
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
#delete specialization can be implemented similarly
class Specialization_delete(GenericAPIView,DestroyModelMixin):
    serializer_class=Specialization_serializer
    queryset=Specializations.objects.all()
    permission_classes=[IsAdminUser]
    def delete(self,request,*args,**kwargs):
        self.destroy(request,*args,**kwargs)
        return Response({'message':"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
