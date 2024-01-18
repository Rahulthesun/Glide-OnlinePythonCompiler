from django.urls import path
from . import views
from .views import CourseList

urlpatterns = [
    path('', views.home , name="home"),
    path("courses/",CourseList.as_view(), name="course_list"),
    path("subunit/<str:pk>" , views.unit_list , name='subunit_list'),
    path("question/<str:pk>", views.question_page , name='question_page'),
    path("answer/<str:pk>", views.answer_code_submit , name='answer_code_submit'),
    ]