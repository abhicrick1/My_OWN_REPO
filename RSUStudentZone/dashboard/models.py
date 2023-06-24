from django.db import models
from datetime import datetime
# Create your models here.

class StudentDetail(models.Model):

# =============================
# Gender
    male = "male"
    female = "female"
    not_to_say = "other"
    gender = [
        (male , "male"),
        (female , "female"),
        (not_to_say, "other",)
    ]
# ==============================


# qualification 
# =============================

    master_degree = "Master Degree"
    bachelors_degree = "Bachelor`s Degree"
    Diploma = "Diploma"
    senior_secondary = "Senior Secondary"
    secondary = "Secondary"
    primary = "Primary"


    hg_qlf = [
        (master_degree, "Master Degree"),
        (bachelors_degree, "Bachelor`s Degree"),
        (Diploma, "Diploma"),
        (senior_secondary, "Senior Secondary"),
        (secondary, "Secondary"),
        (primary, "Primary")
    ]

# ==================================
# Degree Program

    MBA = "MBA"
    MCA = "MCA"
    MCOM = "M.COM"
    MSC = "M.SC"
    MA = "MA"
    MTECH = "M.TECH"
    MBBS = "MBBS"
    ME = "M.E"
    
    BBA = "BBA"
    BCA = "BCA"
    BCOM = "B.COM"
    BSC = "B.SC"
    BA = "MA"
    BTECH = "B.TECH"
    BE = "B.E"



    degree_program = [
        (MBA , "MBA"),
        (MCA , "MCA"),
        (MCOM , "M.COM"),
        (MSC , "M.SC"),
        (MA , "MA"),
        (MTECH , "MTECH"),
        (MBBS , "MBBS"),
        (ME , "ME"),
        (BBA , "BBA"),
        (BCOM , "B.COM"),
        (BSC , "BSC"),
        (BA , "BA"),
        (BTECH , "BTECH"),
        (BE , "BE")
    ]

# =============================================
# Blood Group 

    A = "A+"
    AB = "AB+"
    B = "B+"
    O = "O+"

    A_M = "A-"
    AB_M = "AB-"
    B_M = "B-"
    O_M = "O-"

    blood_group = [
        (A , "A+"),
        (AB , "AB+"),
        (B , "B+"),
        (O , "O+"),
        (A_M , "A-"),
        (B_M , "B-"),
        (AB_M , "AB+"),
        (O, "O-")
    ]

# ==================================================================================================

# Cast
    sc = "sc"
    st = "st"
    obc = "obc"
    gen = "gen"

    category = [
        (sc , "SC"),
        (st , "ST"),
        (obc , "OBC"),
        (gen , "Gen"),
    ]
# ==============================================================================================
# how did you get to know choices
    google_bussiness="Google_Bussiness"
    newspaper="Newspaper"
    social_media="Social_Media"
    friends_relative="Friends OR Relative"

    gtk = [
        (google_bussiness,"Google_Bussiness"),
        (newspaper,"Newspaper"),
        (social_media,"Social_Media"),
        (friends_relative,"Friends OR Relative")


    ]
    
# ==================================================================================================

    enrollment_number = models.CharField(max_length=50, blank=False, null=True, unique=True)
    stu_pic = models.FileField(upload_to="",null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    add_date = models.DateField(null=True, blank=False, default=datetime.now)
    ph1 = models.CharField(max_length=10, blank=False, null=True, unique=True)
    ph2 = models.CharField(max_length=10, blank=True, null=True, unique=False)
    email = models.EmailField(max_length=64, blank=False, null=True, unique=True)
    email2 = models.EmailField(max_length=64, blank=True, null=True, unique=False)
    birth_date = models.DateField(blank=False, null=True)
    gender = models.CharField(max_length=10, blank=True, choices=gender, default=None, null=True)
    blood_group = models.CharField(max_length=10, blank=True, choices=blood_group, default=None)
    city = models.CharField(max_length=100, blank=False, null=True)
    state = models.CharField(max_length=100, blank=False, null=True)
    zip = models.CharField(max_length=8, blank=False, null=True)
    address1 = models.CharField(max_length=255, blank=False, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    student_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=False, null=True)
    father_email1 = models.EmailField(max_length=64, blank=True, null=True, unique=False)
    father_email2 = models.EmailField(max_length=64, blank=True, null=True, unique=False)
    mother_email1 = models.EmailField(max_length=64, blank=True, null=True, unique=False)
    mother_email2 = models.EmailField(max_length=64, blank=True, null=True, unique=False)
    father_occupation = models.CharField(max_length=50, blank=True, null=True)
    father_ph1 = models.CharField(max_length=10, blank=True, null=True)
    father_ph2 = models.CharField(max_length=10, blank=True, null=True)
    mother_occupation = models.CharField(max_length=50, blank=True, null=True)
    mother_ph1 = models.CharField(max_length=10, blank=True, null=True, unique=False)
    mother_ph2 = models.CharField(max_length=10, blank=True, null=True, unique=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=True, unique=True)
    highest_qualification = models.CharField(max_length=50, null=True, blank=True, choices=hg_qlf)
    degree = models.CharField(max_length=50, null=True, blank=True, choices=degree_program)
    pre_school = models.CharField(max_length=100, null=True, blank=True,)
    hdyk_rsu=models.CharField(max_length=50,null=True,choices=gtk)
    category = models.CharField(max_length=100, null=True, blank=True , choices=category)
    created_at = models.DateField(null=True, blank=False, default=datetime.now)
    updated_at = models.DateField(null=True, blank=False, default=datetime.now)

# class Attendence(models.Model):
#     date = models.DateField(blank=False, null=True)
#     attendence_status = models.CharField(max_length=2, blank=False)
#     attendence_remarks = models.CharField(max_length=254, blank=False)
#     task = models.CharField(max_length=254, blank=False, null=True)
#     created_at = models.DateField(null=True, blank=False, default=datetime.now)
#     updated_at = models.DateField(null=True, blank=False, default=datetime.now)

# class Result(models.Model):
#     date = models.DateField(null=True, blank=False)
#     highest_marks = models.IntegerField(null=True, blank=False)
#     obtained_marks = models.IntegerField(null=True, blank=False)
#     min_marks = models.IntegerField(null=True, blank=False)
#     total_marks = models.IntegerField(null=True, blank=False)
#     grade = models.CharField(max_length=50, null=True, blank=False)
#     created_at = models.DateField(null=True, blank=False, default=datetime.now)
#     updated_at = models.DateField(null=True, blank=False, default=datetime.now)

# class Enquiry(models.Model):
#     date = models.DateField(blank=False, null=True)
#     full_name = models.DateField(null=True, blank=False)
#     email = models.EmailField(max_length=150, null=True, blank=False)
#     ph= models.CharField(max_length=10, blank=False, null=True)
#     message = models.TextField(blank=True, null=False)
#     created_at = models.DateField(null=True, blank=False, default=datetime.now)
#     updated_at = models.DateField(null=True, blank=False, default=datetime.now)    

# class Registration(models.Model):
#       name=models.CharField(max_length=100)  
#       username=models.CharField(max_length=100)  
#       email=models.EmailField(max_length=100)  
#       ph=models.CharField(max_length=10)  
#       created_at = models.DateField(null=True, blank=False, default=datetime.now)
#       updated_at = models.DateField(null=True, blank=False, default=datetime.now)

# class Testimonial(models.Model):
#     pic = models.CharField(max_length=50, null=True, blank=False) 
#     name = models.CharField(max_length=50, null=True, blank=False) 
#     message = models.TextField(null=True, blank=False)
#     created_at = models.DateField(null=True, blank=False, default=datetime.now)
#     updated_at = models.DateField(null=True, blank=False, default=datetime.now)

# class StudyMaterial(models.Model):
#     topic = models.FileField(null=True, blank=False)
#     created_at = models.DateField(null=True, blank=False, default=datetime.now)
#     updated_at = models.DateField(null=True, blank=False, default=datetime.now)