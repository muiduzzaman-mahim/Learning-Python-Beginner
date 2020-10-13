#Start Program

#even number
print('Enter The range\nFrom')
i = input()
print('To')
n = input()
count = 0
j = int(i)

print('\nAll even numbers from {} to {}'.format(i,n))
while j <= int(n):
    if j % 2 == 0:
        print(j)
        count = count + 1
    else:
        None 
    j = j + 1
print('There are {} even numbers from {} to {}'.format(count,i,n))

#odd number
j = int(i)
count = 0
print('\nAll odd numbers from {} to {}'.format(i,n))
while j <= int(n):
    if j % 2 == 1:
        print(j)
        count = count + 1
    else:
        None 
    j = j + 1
print('There are {} odd numbers from {} to {}'.format(count,i,n))
#End Program