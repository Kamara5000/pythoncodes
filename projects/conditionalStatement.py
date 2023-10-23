

age = int(input("enter your age"))

if age >= 18:
    print("eligible for vote")

else:
    print("not eligible")

if True:
    print("verified")
else:
    print("not verified")


#printing even number

num = 10

if num%2 == 0:
     print("it is an even number")

print("even number") if num%2 == 0 else print("odd number")

#another example using tenary operator

a=5
{print("hello"), print("python")} if a >=1 else {print("hello"), print("i am not python")}


#using elif for multiple condition

weekno = 1

if weekno == 1:
    print("monday")
elif weekno == 2:
    print("Tuesday")
elif weekno == 3:
    print("wedenesday")
else:
    print("other days")