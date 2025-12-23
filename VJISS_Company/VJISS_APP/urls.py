from django.urls import path
from .views import Create_Users

# endpoints URLS
urlpatterns=[
    path("VJISS/create_user",Create_Users.as_view())
]
