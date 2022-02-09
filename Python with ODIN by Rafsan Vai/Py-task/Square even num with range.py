#start program

r1 = int(input('Enter the range to get even number square\nFrom:\n'))
print('To')
r2 = int(input())

while r1 < r2:
    if r1 % 2 ==0:
        print('sqaure of "{}" is "{}"'.format(r1,r1**2))
    else:
        None
    r1 = r1+1
    
#end Program