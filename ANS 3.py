""" 
3. Write a python program to create 2 objects of the user class and assign different
values.

 """
class user:
    def fun(self,x):
        self.x=x
        print(self.x)
ob=user()
ob.fun(10)
ob2=user()
ob.fun(20)

#=============================OUTPUT=====================================
""" 
10
20
 """
