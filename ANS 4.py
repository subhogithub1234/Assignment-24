""" 
4. Write a python program to init default values for user object using __init__ method.

 """
class user:
    def __init__(self,x=67):
         self.x=x
         print(self.x)

ob=user()
#=================================OUTPUT================================
""" 
67
 """