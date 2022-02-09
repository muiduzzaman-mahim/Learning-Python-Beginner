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

minimum = min(array)

print('Array = {}'.format(array))
print('Minimum number = {}'.format(minimum))

#end