#start program
print('Enter three numbers')

a = int(input())
b = int(input())
c =  int(input())
 
if b>a:
    if c>a:
        print('Less value is {}'.format(a))
    else:
        print('Less value is {}'.format(c))
else:
    if c>b:
        print('Less value is {}'.format(b))
    else:
        print('Less value is {}'.format(c))
 
 
#end Program