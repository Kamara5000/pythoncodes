
#acquiring attributes and behaviour from one class to another

#single inheritance

class A:
    def m1(self):
        print("this is A")

class B(A):
    def m2(self):
        print("this is B")

bob = B()
bob.m1()
bob.m2()

#multilevel inheritance
class A:
    def m1(self):
        print("this is A")

class B(A):
    def m2(self):
        print("this is B")
class C(B):
    def m3(self):
        print("this is c")
bob = C()
bob.m1()
bob.m2()
bob.m3()

#hierachy inheritance
class A:
    def m1(self):
        print("this is A")

class B(A):
    def m2(self):
        print("this is B")

class C(A):
    def m3(self):
        print("this is c")

bob = B()
bob.m1()
bob.m2()

cob =C()
cob.m3()

#mutiple inheritance

class A:
    def m1(self):
        print("this is A")

class B:
    def m2(self):
        print("this is B")

class C(A,B):
    def m3(self):
        print("this is C")

cob =C()
cob.m3()
cob.m2()
cob.m1()

#overiding
class A:
    def m1(self):
        print("this is A")

class B(A):
    def m1(self):
        print("this is B from A")
        super().m1() #this can be use to execute the method in the super class after overriding
bob = B()
bob.m1()

#overriding variables
class Parent:
    name = "scotts"

class Child(Parent):
    name = "yam"
check = Child()
print(check.name)

#overridng method
class Bank:
    def interest(self):
        return 0
class Mbank(Bank):
    def interest(self):
        return 12
myRate = Mbank()
bob = B()
bob.m1()
print(myRate.interest())

#method overloading - this can be use to achoeve polymorphism

class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("hello" + name )
        else:
            print("hello")
h = Human()
h.sayHello("dqv")
h.sayHello()

class Calc:
    def add(self, a=0,b=0,c=0):
        print(a+b+c)
cal = Calc()
cal.add()
cal.add(10,20)
cal.add(92,23,22)