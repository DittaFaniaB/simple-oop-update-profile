from StudentProfile import *
from TeacherProfile import *

def student():
    student_profile = StudentProfile("","",0,0.00)
    print("Input first name, last name, and phone number (split by coma (,))")
    student_profile.first_name,student_profile.last_name,student_profile.phone = input().split(",")
    print("Input GPA : ")
    
    student_profile.gpa = input().split(",")
    print(student_profile.details())
    print(student_profile.cpga_info())
    print(student_profile.completeProfileInfo())

def teachers():
    teacher_profile = TeacherProfile("","",0,0,0)
    print("Input first name, last name, and phone number (split by coma (,))")
    teacher_profile.first_name,teacher_profile.last_name,teacher_profile.phone = input().split(",")
    print("Input attendance and payable amount (split by coma (,))")
    teacher_profile.attendance,teacher_profile.payable_amount = input().split(",")
    
    print(teacher_profile.details())
    print(teacher_profile.teachersPaymentInfo())
    print(teacher_profile.completeProfileInfo())


if __name__ == '__main__':
    print("1. Update Student's profile")
    print("2. Update Teacher's profile")
    if int(input()) == 1:
        student()
    else:
        teachers()