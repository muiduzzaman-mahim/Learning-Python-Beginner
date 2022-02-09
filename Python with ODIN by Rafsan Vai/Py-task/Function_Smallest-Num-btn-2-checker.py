def smallest_num(num1,num2):
    if num1 < num2:
        print('{} is the smallest number'.format(num1))
    else:
        print('{} is the smallest number'.format(num2))

print('\nEnter two numbers to check which is smallest:')
num1 = int(input())
num2 = int(input())

smallest_num(num1, num2)