#start
#3n + 1 Problem using while loop and without array

num = int(input('Enter a number: \n'))

print('Output:')
while num > 1:
    if num % 2 == 0:
        #print('Now, {} is even number. So, {} is divided by 2:-'.format(num,num))
        print('{}/2 ='.format(num), end = ' ')
        num = num // 2
        print('{}\n'.format(num))
    else:
        #print('Now, {} is odd number. So, {} is multiplied by 3 and add 1:-'.format(num,num))
        print('(({}*3)+1) ='.format(num), end = ' ')  # , end = ' ' is used to print without new line
        num = ((num*3)+1)
        print('{}\n'.format(num))

#end