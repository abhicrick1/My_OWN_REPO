from django.shortcuts import render, redirect
from .models import StudentDetail


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def add_student_form(request):
   
    msg = {}
    
    if request.method=="POST":
        
        data = StudentDetail()

        if request.POST.get("enroll_no") == "":
            msg["error"] = "Please Fill Enrollment No."
            

        elif request.POST.get("first_name") == "":
            msg["error"] = "Please Enter Your Name"
            
        elif request.POST.get("email") == "":
            msg["error"] = "Please Enter your Email"
            
        elif request.POST.get("ph_1") == "":
            msg["error"] = "Please Enter Your Phone Number"
            

        elif request.POST.get("dob") == "":
            msg["error"] = "Please Enter Your Date of Birth"
            

        elif request.POST.get("add_1") == "":
            msg["error"] = "Please Enter Your Address"
            

        elif request.POST.get("aadhar_no") == "":
            msg["error"] = "Please Enter your Aadhar No."
            

        elif request.POST.get("father_nm") == "" :
            msg["error"] = "Please Enter your Father`s Name"
            

        elif request.POST.get("mother_nm") == "":
            msg["error"] = "Please enter your Mother`s Name"

        elif request.POST.get("first_name") == "":
            msg["error"] = "Please Enter Your Name"
            

        if request.POST.get("email") == "":
            msg["error"] = "Please Enter your Email"
            
        if request.POST.get("ph_1") == "":
            msg["error"] = "Please Enter Your Phone Number"
            

        if request.POST.get("dob") == "":
            msg["error"] = "Please Enter Your Date of Birth"
            

        if request.POST.get("add_1") == "":
            msg["error"] = "Please Enter Your Address"
            

        if request.POST.get("aadhar_no") == "":
            msg["error"] = "Please Enter your Aadhar No."
            

        if request.POST.get("father_nm") == "" :
            msg["error"] = "Please Enter your Father`s Name"
            

        if request.POST.get("mother_nm") == "":
            msg["error"] = "Please Enter your Mother`s Name"
        
        


        try:
            enroll = StudentDetail.objects.get(enrollment_number = request.POST.get("enroll_no"))
            msg["status"] = "Data can`t be saved due to duplicate value"
            msg["dup_en"] = "Enroll - Already Exsits"
        except:
            data.enrollment_number=request.POST.get("enroll_no")
            
        try:
            email = StudentDetail.objects.get(email = request.POST.get("email"))
            msg["status"] = "Data can`t be saved due to duplicate value"
            msg["dup_em"] = "Email Already Exsits"
        except:
            data.email=request.POST.get("email")

        try:
            phone = StudentDetail.objects.get(ph1 = request.POST.get("ph_1"))
            msg["status"] = "Data can`t be saved due to duplicate value"
            msg["dup_ph"] = "Phone Already Exsits"
        
        except:
            data.ph1=request.POST.get("ph_1")

        try:
            aadhar = StudentDetail.objects.get(aadhar_no = request.POST.get("aadhar_no"))
            msg["status"] = "Data can`t be saved due to duplicate value"
            msg["dup_aadhar"] = "Aadhar Already Exsits"
        
        except:
            data.ph1=request.POST.get("ph_1")


        if len(msg) >=1 :
            pass
        else:
            # data.enrollment_number=request.POST.get("enroll_no")
            data.first_name=request.POST.get("first_name")
            data.middle_name=request.POST.get("middle_name")
            data.last_name=request.POST.get("last_name")
            data.email2=request.POST.get("email_2")
            data.ph2=request.POST.get("ph_2")
            data.birth_date=request.POST.get("dob")
            # obj=time.strftime("%y:%m:%d")
            # print(obj)                                                                      
            data.address1=request.POST.get("add_1")
            data.address2=request.POST.get("add_2") 
            data.student_occupation= request.POST.get("stu_occu")
            data.city=request.POST.get("city")
            data.state=request.POST.get("state")
            data.zip=request.POST.get("zip_code")
            data.stu_pic=request.POST.get("student_pic")
            data.father_name=request.POST.get("father_nm") 
            data.mother_name=request.POST.get("mother_nm")
            data.father_ph1=request.POST.get("father_ph_1")
            data.father_ph2=request.POST.get("father_ph_2")
            data.mother_ph1=request.POST.get("mother_ph_1")
            data.mother_ph2=request.POST.get("mother_ph_2")
            data.father_email1=request.POST.get("father_email_1")
            data.father_email2=request.POST.get("father_email_2")
            data.mother_email1=request.POST.get("mother_email_1")
            data.mother_email2=request.POST.get("mother_email_2")
            data.father_occupation=request.POST.get("father_occup")
            data.mother_occupation=request.POST.get("mother_occup")
            data.gender=request.POST.get("gender")
            data.guardian_name=request.POST.get("guardian_nm")
            data.aadhar_no=request.POST.get("aadhar_no")
            data.highest_qualification=request.POST.get("qulification")
            data.degree=request.POST.get("degree_program")
            data.blood_group=request.POST.get("blood_grp")
            data.category=request.POST.get("category")
            data.pre_school=request.POST.get("pre_school")
            data.hdyk_rsu=request.POST.get("pre_hau")
            
            msg["status"] = "Student Added Sucsessfully"                    
            data.save()




            
        

    return render(request,"dashboard/students/add-student.html", context={"message":msg, "old_data" : request.POST}) 





          

          

def students_list(request):
    student_details = StudentDetail.objects.all()

    return render(request, "dashboard/students/students-list.html",{"student_details": student_details})


