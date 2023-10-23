
# to define a function we use def and end it with :

def myFunc():
    print("hello")

myFunc()

def myFunc(name):
    print("hello", name)
myFunc("Ibrag")

def myFunc(a,b):
    return a+b

print(myFunc(100,222 ))

xy = 200
def cool():
     global xy
     xy = 122 #to convert a global variable into a local variable
     print(xy)
cool()

#we have positional argument and keyworde argumnt

def myFunc(a,b):  #postional argument
    print(a,b)
myFunc(1,3)
myFunc(b = 10, a=2) #keyword argument

def myfunc(i,j=10):
    print(i,j)
myFunc(100,200) #100 rep i while the 10 is replaced by 200
myFunc(100) #since j has a value, the 100 will be assingeg to i

