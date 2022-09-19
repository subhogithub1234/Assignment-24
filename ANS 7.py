""" 
7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).
 """
class Laptop:
    def __init__(self,brand="HP",ram="46",cpu="i7",hdd="2TB"):
         
         self.brand=brand
         self.ram=ram
         self.cpu=cpu
         self.hdd=hdd
    def showConig(self):
        print("Brand:{}, RAM:{}, CPU:{}, HDD:{}".format(self.brand,self.ram,self.cpu,self.hdd))     

ob=Laptop()
ob.showConig()
#=============================OUTPUT====================================
""" 
Brand:HP, RAM:46, CPU:i7, HDD:2TB
 """