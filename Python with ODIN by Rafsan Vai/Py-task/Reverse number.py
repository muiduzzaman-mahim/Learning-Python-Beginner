#start program
#this is only for number

num = int(input('Enter a number to Reverse: \n'))
reverse = 0

while (num > 0):
    
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10

print('Reversed Number = {}'.format(reverse))


#end program