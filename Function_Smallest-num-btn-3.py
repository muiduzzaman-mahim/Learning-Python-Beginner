def smallest_num_3(num1, num2, num3):
    if num1 < num2:
        if num1 < num3:
            print('{} is the smallest number'.format(num1))
        else:
            print('{} is the smallest number'.format(num3))
    else:
        if num2 < num3:
            print('{} is the smallest number'.format(num2))
        else:
            print('{} is the smallest number'.format(num3))
        
print('\nEnter three numbers to check which is smallest among 3:')
num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest_num_3(num1, num2, num3)