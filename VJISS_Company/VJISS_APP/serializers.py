from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from . models import Create_User
from. models import Courses_Model
from . models import Syllabus_Model
from . models import InternshipOffers
from. models import Apply_Internship
from .models import Job_Notifications


class Create_User_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model=Create_User
        fields='__all__'
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Create_User(**validated_data)
        user.set_password(password)  # ✅ hashes password
        user.save()
        return user

class Login_User_Serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
       
        user = authenticate(email=data.get('email'), password=data.get('password'))
        print(data.get('email'))
        print(data.get('password'))
        print(user)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data['user'] = user
        return data 
    


class Syllabus_serializer(serializers.ModelSerializer):
    class Meta:
        model=Syllabus_Model
        fields="__all__"
        
    
class Course_serializer(serializers.ModelSerializer):
    syllabus_courses = Syllabus_serializer(many=True, read_only=True) #provide related_name='syllabus_courses' in models.
    class Meta:
        model=Courses_Model
        fields="__all__"

class InternshipOffers_serializer(serializers.ModelSerializer):
    class Meta:
        model=InternshipOffers
        fields="__all__"
        
class Apply_Internship_serializer(serializers.ModelSerializer):
    internship_offers = InternshipOffers_serializer(read_only=True)
    internship_offers_id = serializers.PrimaryKeyRelatedField(queryset=InternshipOffers.objects.all(),write_only=True, source='internship_offers')
    class Meta:
        model=Apply_Internship
        fields="__all__"

class Job_Notifications_serializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Notifications
        fields="__all__"