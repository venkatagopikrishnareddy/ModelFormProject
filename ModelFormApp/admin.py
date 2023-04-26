from django.contrib import admin
from ModelFormApp.models import Student

# Register your models here.
#admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','marks'];
admin.site.register(Student,StudentAdmin);


