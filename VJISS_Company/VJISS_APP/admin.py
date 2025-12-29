from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Create_User, Courses_Model, Syllabus_Model
from .models import InternshipOffers
from . models import Apply_Internship

@admin.register(Create_User)
class CustomUserAdmin(UserAdmin):
    model = Create_User
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'first_name']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
class CourseAdmin(admin.ModelAdmin):
    list_display=['course_name','course_fee','course_level','course_duration',]

admin.site.register(Courses_Model,CourseAdmin)

class SyllabusAdmin(admin.ModelAdmin):
    list_display=['course_name','module','description']
admin.site.register(Syllabus_Model,SyllabusAdmin)

class InternshipOffersAdmin(admin.ModelAdmin):
    list_display=['internship_name','internship_description','technologies'] 
admin.site.register(InternshipOffers,InternshipOffersAdmin)

class Apply_InternshipAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone_number','internship_offers','education','resume','applied_on','status','reason']    
admin.site.register(Apply_Internship,Apply_InternshipAdmin)