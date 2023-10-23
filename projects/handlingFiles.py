 #writing in a file
f = open("C:/Users/ibrah/Documents/files.txt",'w')
f.write("this is my first write operation...\n")
f.write("this is my first write operation...\n")
f.close()
#w = write, r= read, you have to specify this operation
#reading from the file
f = open("C:/Users/ibrah/Documents/files.txt",'r')
print(f.read()) #read all
print(f.readline())  #read the first line
f.close()

#appending to a file
f = open("C:/Users/ibrah/Documents/files.txt",'a')
f.write("this is new line")
f.close()


