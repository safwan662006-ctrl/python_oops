#this python file is to test all functionality is 
#in future the class will be used to real senerios

from module.student.Student import StudentClass




s1= StudentClass()




#student details

mobile_number = input("enter your mobile number: ")
full_name = input("enter your full name: ")
date_of_birth = input("enter your date of birth: ")
age = int(input("enter your age: "))
gender = input("enter your gender: ")  
email = input("enter your email: ")
preferred_language = input("enter your preferred language: ")
school_college_name = input("enter your school/college name: ")
class_grade = input("enter your class/grade: ")
board_curriculum = input("enter your board/curriculum: ")
academic_year = input("enter your academic year: ")

s1.setStudentDetails(full_name, date_of_birth, age, gender, mobile_number, email, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)

s1.savetoDB()
