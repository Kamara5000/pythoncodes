
class myClaa:
    def myFunc(self):
        pass
    def displ(self, name):
        print("jogn", name)
mc1 = myClaa()
mc1.displ("alex")

#we can call function in a class either through instance method or static
#for static method, you can acess the function in a class directly without
#crreating instance of an object, also self in static method always expect a parameter

class myCl:
    def myFunc(self):
        pass
    def displ(self, name):
        print("jogn", name)
    @staticmethod
    def m(self, num):
        print(self,num)
mc1 = myCl()  #instance method acess through object
mc1.displ("alex")
myCl.m("hello","123")  #staticmethod acess through class

#creating a class variable
class myClassVar:
    a,b=1,2  #class variable
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
mc = myClassVar()
mc.add()
mc.mul()

i,j = 1,2     #global variable
class  myClass:
    a,b = 5,6   #class variable
    def add(self,x,y):   #local variable
        print(x,y)
        print(self.a+self.b)
        print(i,j)

#constructors
#constructor will not return a value

class MyCon:
    def __int__(self):
        print("this is constructor")
    def m2(self):
        print("hello manchester")

con = MyCon()
con.m2()

class MySecond:
    name = "john"
    def __init__(self, name):
        print(name)
        print(self.name)
mx = MySecond("dave")

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def disp(self):
        print(self.ename,self.eid, self.sal)
el = Emp(202,"efrrv",222)
el.disp()
