#start program
#this is only for number

num = int(input('Enter a number to count digits: \n'))
count = 0

while (num > 0):
    num = num // 10
    count += 1
print('There are {} digits in this number'.format(count))

#end program