def smallest_num(num1,num2):
    if num1 < num2:
        print('{} is the smallest number'.format(num1))
    else:
        print('{} is the smallest number'.format(num2))

print('Enter two numbers to check which is smallest:\n')
num1 = int(input())
num2 = int(input())

smallest_num(num1, num2)