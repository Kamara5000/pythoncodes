

#range function
#range(10)  prints 0......10
#range(1,10) prints 1......9
#range(1,10,2) prints starting point  1 to ending point 10 with +2 increment

#list function will shows the values in the range

print(list(range(10)))

print(list(range(5,10)))

print(list(range(1,10,2)))

#printint even number within a range
print(list(range(2,10,2)))

#can print a decrement
print(list(range(10,1,-1)))

#while loop

i=1
while i<=10:
    print(i)
    i=i+1

#descending

i=10
while i>=1:
    print(i)
    i=i-1

#for loop
for i in range (1,11):
    print(i)

#print even number between 0-21
for i in range(0,21,2):
    print(i)

for i in range(10,1,-1):
    print(i)

#Jumping statement

for i in range(1,10):
    if i ==5:
         break
    print(i)
#to skip a number use the continue function
for i in range(1,10):
    if i ==5:
         continue
    print(i)

for i in range(1,10):
    if i ==5 or i==7 or i==3:
         continue
    print(i)