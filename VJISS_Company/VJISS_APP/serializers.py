from rest_framework import serializers
from django.contrib.auth.hashers import check_password

from . models import Create_User

class Create_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Create_User
        fields='__all__'
class Login_User_Serializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField(max_length=10,write_only=True)
    class Meta:
        model=Create_User
        fields=['email','password']

    def validate(self,data):
        email=data.get('email')
        password=data.get('password')
        if not email or not password:
            raise serializers.ValidationError("both feild are required ")
        try :
            user=Create_User.objects.get(email=email)
        except Create_User.DoesNotExist as e:
            
            raise serializers.ValidationError("Invalid email or password")
        if not check_password(password,user.password):
            raise serializers.ValidationError("Invalid email and password")
        data['user']=user
        return data 
        