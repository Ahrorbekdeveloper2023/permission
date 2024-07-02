from django.shortcuts import render
from .models import Courses, Teacher, Students
from .serializer import CoursesSerializer, TeacherSerializer, StudentsSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated



class CourseCreateAPIView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class CourseUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class TeacherCreateAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class StudentsCreateAPIView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class StudentsUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.DjangoModelPermissions]