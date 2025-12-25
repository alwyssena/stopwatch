from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password



# Create your models here.


def validator_password_length(value):
    if len(value)<8:
        raise ValidationError("password must be at least 8 characters long ")

# create users
class Create_User(models.Model):

    public_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name=models.CharField(max_length=100,blank=False,null=False)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,blank=False,null=False)
    phone_number=models.CharField(max_length=15,unique=True,blank=False,null=False)
    password=models.CharField(max_length=255,validators=[validator_password_length])
    confirm_password=models.CharField(max_length=255,validators=[validator_password_length])
    gender_choices=[('M','Male'),('F','Female'),('O','Other')]
    gender=models.CharField(max_length=6,choices=gender_choices,default='Male')
    date_of_birth=models.DateField()
    Required_fileds=['first_name','email','phone_number','password','confirm_password','gender','date_of_birth']

    def save(self,*args,**kwargs):
        if self.password != self.confirm_password:
            raise ValidationError("password do not match")
        if not self.password.startswith('pbkdf2_'):
            self.password=make_password(self.password)
            self.confirm_password= self.password
        super(Create_User, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.public_id)
    
class Courses_Model(models.Model):
    public_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course_name=models.CharField(max_length=100)
    course_log=models.ImageField(upload_to='course_logos/')
    course_duration=models.CharField(max_length=50)
    course_description=models.TextField()
    level_choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')]
    course_level=models.CharField(max_length=20,choices=level_choices,default='Beginner')
    def __str__(self):
        return str(self.public_id)