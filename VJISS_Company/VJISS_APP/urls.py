from django.urls import path
from .views import Create_Users,Login
from .views import AddCourse

# endpoints URLS
urlpatterns=[
    path("VJISS/create_user",Create_Users.as_view()),
    path("VJISS/login",Login.as_view()),
    path("VJISS/add_course",AddCourse.as_view()),
]
