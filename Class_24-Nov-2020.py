import random

#creating file
with open('File/numberlist.txt', 'a+') as fileToBeWrite:
    listA = random.sample(range(0,50),40)
    print(listA)

    for i in listA:
        if (expression):
            pass