from rest_framework import serializers
from . models import Create_User

class Create_User_serializer(serializers.ModelSerializer):
    class Meta:
        model=Create_User
        fields='__all__'