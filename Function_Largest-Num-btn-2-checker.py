def largest_num(num1,num2):
    if num1 > num2:
        print('{} is the largest number'.format(num1))
    else:
        print('{} is the largest number'.format(num2))

print('Enter two numbers to check which is largest:\n')
num1 = int(input())
num2 = int(input())

largest_num(num1, num2)