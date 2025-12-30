from django.urls import path
from .views import Create_Users,Login
from .views import AddCourse
from .views import Course_details,Course_modify,Course_delete
from .views import AddSyllabus,SyllabusModify,SyllabusDelete
from .views import InternshipOffers_modify,InternshipOffers_delete, AddInternshipOffers,InternshipOffers_details  
from .views import InternshipApplication,ViewApplications,ModifyApplication,DeleteApplication
from .views import AddJobNotification,JobNotificationDetails,JobNotificationModify,JobNotificationDelete

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
    path("VJISS/add_internship_offers",AddInternshipOffers.as_view()),
    path("VJISS/internship_offers_details",InternshipOffers_details.as_view()),
    path("VJISS/modify_internship_offers/<str:pk>",InternshipOffers_modify.as_view()),
    path("VJISS/delete_internship_offers/<str:pk>",InternshipOffers_delete.as_view()),
    path("VJISS/apply_internship",InternshipApplication.as_view()),
    path("VJISS/view_applications",ViewApplications.as_view()),
    path("VJISS/modify_application/<str:pk>",ModifyApplication.as_view()),
    path("VJISS/delete_application/<str:pk>",DeleteApplication.as_view()),
    path("VJISS/add_job_notification",AddJobNotification.as_view()),
    path("VJISS/job_notification_details",JobNotificationDetails.as_view()),
    path("VJISS/modify_job_notification/<str:pk>",JobNotificationModify.as_view()),
    path("VJISS/delete_job_notification/<str:pk>",JobNotificationDelete.as_view()),
]
        