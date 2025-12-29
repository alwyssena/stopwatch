from django.urls import path
from .views import Create_Users,Login
from .views import AddCourse
from .views import Course_details,Course_modify,Course_delete
from .views import AddSyllabus,SyllabusModify,SyllabusDelete

# endpoints URLS
urlpatterns=[
    path("VJISS/create_user",Create_Users.as_view()),
    path("VJISS/login",Login.as_view()),
    path("VJISS/add_course",AddCourse.as_view()),
    path("VJISS/course_details",Course_details.as_view()),
    path("VJISS/course_modify/<str:pk>",Course_modify.as_view()),
    path("VJISS/course_delete/<str:pk>",Course_delete.as_view()),
    path("VJISS/add_syllabus",AddSyllabus.as_view()),
    path("VJISS/modify_syllabus/<str:pk>",SyllabusModify.as_view()),
    path("VJISS/delete_syllabus/<str:pk>",SyllabusDelete.as_view()),
]
