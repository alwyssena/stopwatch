from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(email, password, **extra_fields)

class Create_User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
   
    
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    date_of_birth = models.DateField()
    
    # ALL REQUIRED FIELDS 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # ← REQUIRED BY PermissionsMixin
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Fix related_name conflicts
    groups = models.ManyToManyField(Group, related_name='vjiss_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='vjiss_users', blank=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone_number', 'date_of_birth']

    def __str__(self):
        return f"{self.email}\t ({self.public_id})"


    
class Courses_Model(models.Model):
    course_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course_name=models.CharField(max_length=100)
    course_log=models.ImageField(upload_to='course_logos/')
    course_duration=models.CharField(max_length=50)
    course_fee=models.IntegerField()
    course_description=models.TextField()
    level_choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')]
    course_level=models.CharField(max_length=20,choices=level_choices,default='Beginner')
    def __str__(self):
        return  f"{self.course_name}\t ({self.course_id})"
class Syllabus_Model(models.Model):
    syllabus_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course_name=models.ForeignKey(Courses_Model,on_delete=models.CASCADE,related_name='syllabus_courses')
    module=models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return str(self.syllabus_id)

#Specializations Model

class InternshipOffers(models.Model):
    internship_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    internship_name=models.CharField(max_length=100)
    internship_description=models.TextField()
    technologies=models.CharField(max_length=200)
    def __str__(self):
        return str(self.internship_id)

#intership model 
class Apply_Internship(models.Model):
    application_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name =models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    internship_offers=models.ForeignKey(InternshipOffers,on_delete=models.CASCADE,related_name='internship_offers')
    education_choices=[('Diploma', 'Diploma'),('UG', 'Under Graduate'),('PG', 'Post Graduate'),('PhD', 'PhD'),]
    education=models.CharField(max_length=200,choices=education_choices)
    resume=models.FileField(upload_to='resumes/')
    applied_on=models.DateTimeField(auto_now_add=True)
    status_choices=[('Pending','Pending'),('Accepted','Accepted'),('Rejected','Rejected')]
    status=models.CharField(max_length=20,choices=status_choices,default='Pending')
    reason=models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.application_id)

#job notifications model
class Job_Notifications(models.Model):
    notification_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    company_logo=models.ImageField(upload_to='company_logos/')
    job_title=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    job_description=models.TextField()
    requirements=models.TextField()
    link=models.URLField()
    def __str__(self):
        return str(self.notification_id)