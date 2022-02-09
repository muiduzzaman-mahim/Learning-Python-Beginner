#start program
print('Enter three numbers')

a = int(input())
b = int(input())
c = int(input())
 
if b<a:
    if c<a:
        print('Greater value is {}'.format(a))
    else:
        print('Greater value is {}'.format(c))
else:
    if c<b:
        print('Greater value is {}'.format(b))
    else:
        print('Greater value is {}'.format(c))
 
 
#end Program