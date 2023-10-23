

num1 = 10
num2 = 10.0

print(type(num1))
print(type(num2))

#max prints maximum whilw min prints minimum

print(max(1,23,2,2,122,1,))
print(min(1,23,2,2,122,1,))

#strings operetions different ways to declare a string including an empty string
s = "hello"
a = ""
x = str("error")
y = ''
z = str('come')
t = str()

#concatenation
print("hello" + "my boy")
print("hello" *3)

#slicing[]
#starting index 0, ending index 1

str = "welcome"
print(str[1:3])
print(str[:3]) #this means starting index is 0 and end at 3
print(str[2:]) #starting is 2 and ending is t# he last index
print(str[2:-1]) # starting index is 2 and the index is last index-1

#max, min and len operation

print(max("abc"))
print(min("abc"))
print(len("abc"))

#in return true or false

s= "welcome"

print("come" in s) #return true because come is a subset of welcome
print("lome" in s) #return false because lome is not a subset of welcome

#testing strings
s= "welcome"
print(s.isalnum()) #return false since all is not a number
print(s.isalpha()) #retuen true simce all is alphabelt
print(s.isspace()) #check is there is space and return true is there is
print(s.isupper()) # check is its upper case

#searching within string

s = "welcome to python"
print(s.endswith("thon")) #check if it ends with "thon" and return true if true
print(s.startswith("good")) #check if it starts with "good" in this example it returns false

print(s.find("come")) #return  3 becuase it has come within the string and find at index 3
print(s.count("o")) #return the number of time the substring "o" appers

#converting string
s = "weCome to london"

s1 = s.capitalize()

s2 = s.title()

s3 = s.swapcase()

s4 = s.replace("in", "on")

#reverse a string
s = "welcome"
rev_str = ''

for i in s:
    rev_str = i+rev_str
print("reversed string is" , rev_str)

#another example
s= "welcome"
rev_str = s[::-1]
print(rev_str)