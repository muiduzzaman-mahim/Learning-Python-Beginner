def largest_num_3(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print('{} is the largest number'.format(num1))
        else:
            print('{} is the largest number'.format(num3))
    else:
        if num2 > num3:
            print('{} is the largest number'.format(num2))
        else:
            print('{} is the largest number'.format(num3))
        
print('Enter three numbers to check which is largest among 3:\n')
num1 = int(input())
num2 = int(input())
num3 = int(input())

largest_num_3(num1, num2, num3)