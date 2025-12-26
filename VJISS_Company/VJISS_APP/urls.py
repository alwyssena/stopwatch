from django.urls import path
from .views import Create_Users,Login
from .views import AddCourse
from .views import Course_details

# endpoints URLS
urlpatterns=[
    path("VJISS/create_user",Create_Users.as_view()),
    path("VJISS/login",Login.as_view()),
    path("VJISS/add_course",AddCourse.as_view()),
    path("VJISS/course_details",Course_details.as_view()),
]
