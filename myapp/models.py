from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# =========================
# Custom User
# =========================
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('principal', 'Principal'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

# =========================
# Student
# =========================
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student")
    roll_number = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    shift = models.CharField(max_length=10)

    def __str__(self):
        return self.user



# =========================
# Teacher
# =========================
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher")
    name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# =========================
# Attendance
# =========================
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')]
    )

    class Meta:
        unique_together = ('student', 'subject', 'date')

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject} - {self.date} - {self.status}"


class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks = models.FloatField()
    total_marks = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)



from django.db import models
from django.conf import settings

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('notice', 'Notice'),
        ('assignment', 'Assignment'),
        ('exam', 'Exam Info'),
        ('message', 'Message'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='notice')
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.category})"
