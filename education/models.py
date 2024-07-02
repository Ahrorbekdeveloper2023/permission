from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='active')
    experience = models.CharField(max_length=100)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.full_name

class Students(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    parents_phone_number = models.CharField(max_length=13)
    telegram_link = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='students')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.full_name
