#start program

num = int(input('Enter a number to count unique numbers: \n'))
temp = [200]
i = 0

while(num > 0):
    digit = num % 10
    num = num // 10
    print(digit)

while(i >= 0):
    temp[i] = digit
    i =+1

#end program