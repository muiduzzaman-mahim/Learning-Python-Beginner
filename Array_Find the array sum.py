#start

array = []
n = int(input('Enter the length of array: \n'))
i = 0
print('Please enter the elements of Array:')

# array = [1,2,3,4,5,6] #use this when there is no need user input.

while i < n:
    element = float(input())
    array.append(element)
    i = i+1

i = 0
sum = 0
while i < len(array):
    sum = sum + array[i]
    i = i+1

print('Array = {}'.format(array))
print('Sum of The elements of Array = {}'.format(sum))

#end