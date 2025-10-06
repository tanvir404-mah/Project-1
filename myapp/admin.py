from django.contrib import admin
from .models import Student, Teacher
from django.contrib.auth.admin import UserAdmin

admin.site.register(Student)
admin.site.register(Teacher)
# Register your models here.
# from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin
# admin.site.register(CustomUser, UserAdmin)
