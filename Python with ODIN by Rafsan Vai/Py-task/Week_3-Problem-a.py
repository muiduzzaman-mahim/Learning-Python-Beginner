# problem (a)
# write a code that will create a file in a folder
# populapte some lines and apppend it to newly created file
# read the whole file
# reverse the file and append it to the file

#start

from os import read

#create file with some lines
def create():
    print('Created file with some lines\n')
    f = open("Muiduzzaman Mahim-file.txt", "w+")
    for i in range(5):
        f.write("Line no: --> %d\n" % (i+1))
    f.close()

#append new lines inside this file
def append():
    print('Now, appended new lines inside this file\n')
    f = open("Muiduzzaman Mahim-file.txt", "a+")
    for i in range(5):
        f.write("Here, new Appended Line no: --> %d\n" % (i+1))  
    f.close()  

#read and print the whole file
def read():
    print('Now, Read and printed the whole file\n')
    f = open("Muiduzzaman Mahim-file.txt", "r")
    if f.mode == "r":
        content = f.read()
        print(content)
    f.close()

#Reverse the file line and append again
def reverse_append():
    print('Reversed lines and appended again\n')
    f = open("Muiduzzaman Mahim-file.txt","r")
    f_a = open("Muiduzzaman Mahim-file.txt","a+")
    lines = f.readlines()
    reversed_line = reversed(lines)
    for i in reversed_line:
        reversed_file = i.rstrip()
        f_a.write('\n{}'.format(reversed_file))
        print(reversed_file)    
    f.close()


create()
append()
read()
reverse_append()
print('\n\nFile is finally closed')

#end