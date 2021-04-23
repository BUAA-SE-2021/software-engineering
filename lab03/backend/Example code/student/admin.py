from django.contrib import admin
from student.models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'password']


admin.site.register(Student, StudentAdmin)
