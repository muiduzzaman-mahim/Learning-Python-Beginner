#start
range1 = int(input('Enter a range.\nFrom '))
range2 = int(input('To '))
range1_init = range1
sum = 0

while range1 <= range2:
    if range1 % 2 == 0:
        print('{}+{} ='.format(sum,range1), end=' ')
        sum = sum + range1
        print(sum)
    else:
        None 
    range1 = range1 + 1
print('sum of all even numbers form {} to {} = {}'.format(range1_init,range2,sum))

#end