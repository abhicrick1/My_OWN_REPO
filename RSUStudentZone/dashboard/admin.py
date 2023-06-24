from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.StudentDetail)
class AdminStudentDetails(admin.ModelAdmin):
    list_display = ["enrollment_number","stu_pic","first_name","middle_name","last_name","add_date","ph1","ph2","email","email2","birth_date",
                    "gender","blood_group","city","state","zip","address1","address2","student_occupation",
                    "father_name","mother_name","guardian_name","father_email1","father_email2","mother_email1","mother_email2",
                    "father_occupation","father_ph1","father_ph2","mother_occupation","mother_ph1","mother_ph2","aadhar_no","highest_qualification",
                    "degree","pre_school","hdyk_rsu","category","created_at","updated_at"]
    
# @admin.register(models.Attendence)
# class Attendence(admin.ModelAdmin):
#     list_display = [
#                     "date", "attendence_status", "attendence_remarks", "task", "created_at", "updated_at"
#                     ]

# @admin.register(models.Result)
# class Result(admin.ModelAdmin):
#     list_display = [
#                     "date", "highest_marks", "obtained_marks", "min_marks", "total_marks", "grade","created_at", "updated_at"
#                     ]
    
# @admin.register(models.Enquiry)
# class Enquiry(admin.ModelAdmin):
#     list_display = [
#                     "date", "full_name", "email", "ph", "message", "created_at","updated_at"
#                     ]
    
    
# @admin.register(models.Registration)
# class Registration(admin.ModelAdmin):
#     list_display = [
#                     "name", "username", "email", "ph", "created_at", "updated_at"
#                     ]
    
    
# @admin.register(models.Testimonial)
# class Testimonial(admin.ModelAdmin):
#     list_display = [
#                     "pic", "name", "message", "created_at", "updated_at"
#                     ]
    
# @admin.register(models.StudyMaterial)
# class StudyMaterial(admin.ModelAdmin):
#     list_display = [
#                     "topic","created_at", "updated_at"
#                     ]