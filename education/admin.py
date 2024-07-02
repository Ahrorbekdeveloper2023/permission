from django.contrib import admin
from .models import Courses, Teacher, Students


admin.site.register([Courses, Teacher, Students])