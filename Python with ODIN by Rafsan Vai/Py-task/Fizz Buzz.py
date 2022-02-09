#start

num = float(input('Enter a number to identify fizz buzz: \n'))

if num % 3 == 0:
    if num % 5 == 0:
        print('{} is a "Fizz Buzz" Number'.format(num))
    else:
        print('{} is a "Fizz" Number'.format(num))
else:
    if num % 5 == 0:
        print('{} is a "Buzz" Number'.format(num))
    else:
        print('{} is neither "Fizz" nor "Buzz" Number'.format(num))
#end 