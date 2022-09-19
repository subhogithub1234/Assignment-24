""" 
5. Write a python program to delete the age property of the user.
 """
class user:
    name='Subham'
    age='22'
    email='abcd@gmail.com'
print(user.name)    
del user.age
print(user.age)
print(user.email)

#=============================OUTPUT-1====================================
""" 
Subham
abcd@gmail.com
 """
#=============================OUTPUT-2==================================== 
#AttributeError: type object 'user' has no attribute 'age'