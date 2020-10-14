#start program

r1 = int(input('Enter the range\nFrom:\n'))
print('To')
r2 = int(input())
i = r1
count = 0

while i < r2:
    if i%5 == 0:
        if i%7 == 0:
            print('{} is divided by 5 and 7'.format(i))
            count = count+1
        else:
            None
    else:
        None
    i = i+1
print('There are {} numbers divided by 5 and 7 from {} to {}'.format(count,r1,r2))

#end Program