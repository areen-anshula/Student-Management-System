from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.StudentListCreate.as_view(), name='StudentListCreate'),
    path('students/<int:pk>/', views.StudentDetails.as_view(), name="StudentDetail"),
]

