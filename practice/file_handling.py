import os
#PYTHON READ AND OPEN FLIES
f = open("test.txt", "r")
# print(f.read())  This is used to read the enter txt file
#print(f.read(5)) You can also specify the amount of characters you want to be returned using 
print(f.readline()) #This is used to read a single line of the txt file. It can be called multiple times

#You can also read a txt file by looping through the line of the file
# for x in f:
#     print(x)

#It is necessary to alays close a file after you are done reading it
f.close()

#You can also use the with statement to open, read and close a file
with open("test2.txt", "r") as t:
    print(t.read())


#PYTHON APPEND, WRITE AND CREATE FILES
#Appending file "a" It will normally add the text to the end of the txt file if the file exist
ar = open("text.txt", "a")
ar.write("Now it is time to do the writing")
ar.close()

ar = open("text.txt")
print(ar.read())

#Writing file "w". Note: It overwrite the entire txt file been called
wr = open("test.txt", "w")
wr.write("I mistakenly overwrite the test.txt instead of the text.txt")
wr.close()

wr = open("test.txt")
print(wr.read())

#Creating file "x". Note: It will return error if the file already exist
# xr = open("myfile.txt", "x") This crate a new file
# xr = open("text.txt", "x") This will return an error

#PYTHON DELETE FILES. You will have to import os
# os.remove("myfile.txt") This will delete the txt file
#Checking if a file exist before tryong to delete it to avoid error
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("This file doesn't exist")
#To delete a folder
#os.rmdir("myfolder")