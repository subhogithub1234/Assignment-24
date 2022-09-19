""" 
9. Write a python program to create a School class and 3 instance variables and 1 class
variable.
 """
class School:
    name="Ushagram Boys High School"
    print(name)
    def __init__(self,student_name,roll,standard):
         self.student_name=student_name
         self.roll=roll
         self.standard=standard
         print(self.student_name,self.roll,self.standard,sep="\n")
ob=School("Subham Chakraborty",6,"XI")

