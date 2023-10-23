
#List,tuple,set,dictionary

#List - a list is a type of collection which is ordered and  changeable
#they are written by a square bracket []

myList = [10,20,30]
myList = ['ss','ss', 'ww']
myList = ['aa', 12, 'ww']
myList = []

#list can be number, string or combination or an empty list as depicted above

#assesing items from the list

myList = ["apple", "banna", "cherry"]
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[-1])

myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
print(myList[2:5])  #prints the items within the range of index2 and 5
print(myList[-4:-1]) #-1 means the last items and -4 is calculated backaward from the last item

#changing item value
myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
myList[0] = "orange"

#reading item in a list
myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
for i in myList:
    print(i)

#check if item is present
if "apple" in myList:
    print("present")
else:
    print("not present")

#list length
print(len(myList))

#adding new item to the list
myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
myList.append("book")
print(myList)

#inserting to a specific index
myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
myList.insert(1,"book")
print(myList)

#remove item from the list
myList.pop(0) #remove item at that index

del myList[2] #

myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
myList.clear() #this will remove all the items

#copy list
myList = ["apple", "banna", "cherry", "dog", "car", "brush", "eat"]
myList2 = list(myList)

#or using copy option
myList2 = myList.copy()

#joining list
myList3 = myList+myList #using + operator

    #using loop statement
for i in myList2:
    myList.append(i)
print(myList)

#using extend function
myList.extend(myList2)


#Tuple - a tuple is a type of collection which is ordered and  unchangeable
#they are written by a round bracket ()
#it is immutable

myTuple = ("banna", "mango", "tree","apple", "banna", "cherry", "dog", "car", "brush", "eat")
print(myTuple)
print(myTuple[1])
print(myTuple[-1])
print(myTuple[2:5])
print(myTuple[-4:-1])

#in tuple you cant modify, append, insert

#the only solution is to convert to a list then reconvert to tuple
myTuple = ("apple", "banna", "cherry", "dog", "car", "brush", "eat")
myList = list(myTuple)
myList[0] = "ball"

myTuple= tuple(myList)
print(myTuple)

#reading item in a tuple
myTuple = ("apple", "banna", "cherry", "dog", "car", "brush", "eat")
for i in myTuple:
    print(i)

#check if item is present
if "banna" in myTuple:
    print("verified")
else:
    print("not verified")

#total number of items in a tuple
print(len(myTuple))

#copy a tuple
myTuple = ("apple", "banna", "cherry", "dog", "car", "brush", "eat")

myTuple2 = myTuple

#joining of tuple
myTuple3 = myTuple + myTuple2

#compare tuple

if myTuple3 == myTuple:
    print("equal")
else:
    print("not equal")



#Sets
#A collection which is unordered and unindexed. they are written in curly bracket

mySet = {"banna", "apple", "cherrry"}
for i in mySet:
    print(i)
#checking an item
print("banna" in mySet) #retuen true

#adding item to a set
mySet.add("orange")
#add will only add single item while update can addd multiple items
mySet.update(["mango", "juice"])
print(mySet)

#check length
print(len(mySet))

#remove item
mySet.remove("orange")
print(mySet)

mySet.discard("orange") # the discard method will not throw error if the item does not initially present in the set

#clear all items in a set
mySet.clear()

#delete a set
del mySet

#join two set
mySet = {"banna", "apple", "cherrry"}
mySet2 = {"banna", "apple", "cherrry"}

mySet3 = mySet .union(mySet2)

#update set
# mySet.update(1,2,3) #add the value directly or below
mySet.update(mySet2)

#Dictionary
#collection that is unordered, changeable and indexed. written in curly bracket with key value pair

myDict = {1:'x', 2:'y', 3:'z'}
print(myDict)

myDict1 = {
    "name":"Alex",
    "age": 110,
    "status": "single"
}
#acessing item
print(myDict1["name"])

print(myDict1.get("name"))

#changing value
myDict1["name"] = "Bisi"
print(myDict1)

#reading item using loop
for i in myDict1:
    print(i)  #print only keys
for i in myDict1:
    print(myDict1[i]) #print only value
for i in myDict1.values():
    print(i) #print only values
for i,j in myDict1.items():
    print(i,j) #print both key and value

#check if a key exist
if "age" in myDict1:
    print("available")
#number of items in a dictionary
print(len(myDict1))

#adding item to dictionary
myDict1["height"] = 12
print(myDict1)

#remove item
myDict1.pop("age")

del myDict1["name"] #this can also be use to remove item

#delete dictionary
#   del myDict1

#clear the dictionary
#myDict1.clear()

#copy
myDict = myDict1

myDict = myDict1.copy()

print(myDict)


