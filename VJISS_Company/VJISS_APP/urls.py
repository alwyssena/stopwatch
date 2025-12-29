from django.urls import path
from .views import Create_Users,Login
from .views import AddCourse
from .views import Course_details,Course_modify,Course_delete
from .views import AddSyllabus,SyllabusModify,SyllabusDelete
from .views import AddSpecialization
from .views import Specialization_details,Specialization_modify,Specialization_delete

# endpoints URLS
urlpatterns=[
    path("VJISS/create_user",Create_Users.as_view()),
    path("VJISS/login",Login.as_view()),
    path("VJISS/add_course",AddCourse.as_view()),
    path("VJISS/course_details",Course_details.as_view()),
    path("VJISS/modify_course/<str:pk>",Course_modify.as_view()),
    path("VJISS/delete_course/<str:pk>",Course_delete.as_view()),
    path("VJISS/add_syllabus",AddSyllabus.as_view()),
    path("VJISS/modify_syllabus/<str:pk>",SyllabusModify.as_view()),
    path("VJISS/delete_syllabus/<str:pk>",SyllabusDelete.as_view()),
    path("VJISS/add_specialization",AddSpecialization.as_view()),
    path("VJISS/specialization_details",Specialization_details.as_view()),
    path("VJISS/modify_specialization/<str:pk>",Specialization_modify.as_view()),
    path("VJISS/delete_specialization/<str:pk>",Specialization_delete.as_view()),
]
        