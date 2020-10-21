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
pos = 0
pos_list = []
while i < n:
    if array[i] > 0:
        pos = pos+1
        pos_list.append(array[i])
    i = i+1

print('Array = {}'.format(array))
print('Total Positive numbers = {}'.format(pos))
print('List of Positive Numbers = {}'.format(pos_list))

#end