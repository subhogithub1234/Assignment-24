""" 
6. Write a python program to create 3 user objects and find the youngest of all.
 """
class user:
     def __init__(self,marks):
        self.marks=marks
     def compare(self,other):
         self.r=min(self.marks,other.marks)
         print(self.r)
ob=user(67)
ob2=user(42)
ob.compare(ob2)  
#================================OUTPUT==============================
# 42      

