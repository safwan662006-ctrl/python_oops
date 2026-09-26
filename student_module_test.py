#this python file is to test all functionality is 
#in future the class will be used to real senerios

from module.student.Student import StudentClass


#student registration test

email = input("enter your email: ")
password = input("enter your password: ")


s1= StudentClass()
s1.SetUserName(email, password)