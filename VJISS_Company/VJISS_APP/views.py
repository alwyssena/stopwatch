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

from . serializers import InternshipOffers_serializer
from . models import InternshipOffers

from . serializers import Apply_Internship_serializer
from . models import Apply_Internship

from .models import Job_Notifications
from .serializers import Job_Notifications_serializer

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
# update user details

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from .models import Create_User
from .serializers import Create_User_Serializer


class Update_Password(GenericAPIView, UpdateModelMixin):
    serializer_class = Create_User_Serializer
    queryset = Create_User.objects.all()

    def get_object(self):
        email = self.request.data.get("email")
        phone_number = self.request.data.get("phone_number")

        if not email or not phone_number:
           return None

        try:
            return Create_User.objects.get(
                email=email,
                phone_number=phone_number
            )
        except Create_User.DoesNotExist:
            return None
    def put(self, request, *args, **kwargs):
        user = self.get_object()

        if user is None:
            return Response(
                {"error": "Invalid email or phone number"},
                status=status.HTTP_404_NOT_FOUND
            )

        new_password = request.data.get("new_password")

        if not new_password:
            return Response(
                {"error": "New password is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Password updated successfully"},
            status=status.HTTP_200_OK
        )

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

        
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

# InternshipOffers can be added here similarly
class AddInternshipOffers(GenericAPIView,CreateModelMixin):
    serializer_class=InternshipOffers_serializer
    permission_classes=[IsAdminUser]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

#retive internship offers can be implemented similarly
class InternshipOffers_details(GenericAPIView,ListModelMixin):
    serializer_class=InternshipOffers_serializer
    queryset=InternshipOffers.objects.all()
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
#modify internship offers
class InternshipOffers_modify(GenericAPIView,UpdateModelMixin):
    serializer_class=InternshipOffers_serializer
    queryset=InternshipOffers.objects.all()
    permission_classes=[IsAdminUser]
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
#delete internship offers can be implemented similarly
class InternshipOffers_delete(GenericAPIView,DestroyModelMixin):
    serializer_class=InternshipOffers_serializer
    queryset=InternshipOffers.objects.all()
    permission_classes=[IsAdminUser]
    def delete(self,request,*args,**kwargs):
        self.destroy(request,*args,**kwargs)
        return Response({'message':"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)

# internship application view

class InternshipApplication(GenericAPIView,CreateModelMixin):
    serializer_class=Apply_Internship_serializer
    print("internship application api hiting")
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        print(request.data)
        return self.create(request,*args,**kwargs)
#view to see all applications (admin only)
class ViewApplications(GenericAPIView,ListModelMixin):
    serializer_class=Apply_Internship_serializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Apply_Internship.objects.all()
        print("Logged in email:", self.request.user.email)
        return Apply_Internship.objects.filter(email=self.request.user.email)
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
#modify application
class ModifyApplication(GenericAPIView,UpdateModelMixin):
    serializer_class=Apply_Internship_serializer
    queryset=Apply_Internship.objects.all()
    permission_classes=[IsAdminUser]
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs) 
  #delete application   
class DeleteApplication(GenericAPIView,DestroyModelMixin):
    serializer_class=Apply_Internship_serializer
    queryset=Apply_Internship.objects.all()
    permission_classes=[IsAdminUser]
    def delete(self,request,*args,**kwargs):
        self.destroy(request,*args,**kwargs)
        return Response({'message':"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)

# job notifications can be added here similarly
class AddJobNotification(GenericAPIView,CreateModelMixin):
    serializer_class=Job_Notifications_serializer
    permission_classes=[IsAdminUser]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
#job notification view can be added here similarly
class JobNotificationDetails(GenericAPIView,ListModelMixin):
    serializer_class=Job_Notifications_serializer
    queryset=Job_Notifications.objects.all()
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
#jon notification modify 
class JobNotificationModify(GenericAPIView,UpdateModelMixin):
    serializer_class=Job_Notifications_serializer
    queryset=Job_Notifications.objects.all()
    permission_classes=[IsAdminUser]
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

#job notification delete can be implemented similarly
class JobNotificationDelete(GenericAPIView,DestroyModelMixin):
    serializer_class=Job_Notifications_serializer
    queryset=Job_Notifications.objects.all()
    permission_classes=[IsAdminUser]
    def delete(self,request,*args,**kwargs):
        self.destroy(request,*args,**kwargs)
        return Response({'message':"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)