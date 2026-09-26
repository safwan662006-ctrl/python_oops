#this python file is to test all functionality is 
#in future the class will be used to real senerios

from module.student.Student import StudentClass


#student registration test

email = input("enter your email: ")
password = input("enter your password: ")


s1= StudentClass()
s1.SetUserName(email, password)



#student details

mobile_number = input("enter your mobile number: ")
full_name = input("enter your full name: ")
date_of_birth = input("enter your date of birth: ")
gender = input("enter your gender: ")  
s1.SetStudentDetails(full_name, date_of_birth, gender, mobile_number, email, password)
