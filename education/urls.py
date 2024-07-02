from django.urls import path, include
from .views import (CourseCreateAPIView, CourseUpdateDeleteAPIView, TeacherCreateAPIView,
                     TeacherUpdateDeleteAPIView, StudentsCreateAPIView, StudentsUpdateDeleteAPIView)
app_name = 'education'

urlpatterns = [
    path('api/v1/courses/', CourseCreateAPIView.as_view(), name='courses_create'),
    path('api/v1/courses/<int:pk>/', CourseUpdateDeleteAPIView.as_view(), name='courses_update_delete'),

    path('api/v1/teacher/', TeacherCreateAPIView.as_view(), name='teacher_create'),
    path('api/v1/teacher/<int:pk>/', TeacherUpdateDeleteAPIView.as_view(), name='teacher_update_delete'),

    path('api/v1/students/', StudentsCreateAPIView.as_view(), name='students_create'),
    path('api/v1/students/<int:pk>/', StudentsUpdateDeleteAPIView.as_view(), name='students_update_delete'),

    path('api-auth/', include('rest_framework.urls')),
]