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
neg = 0
neg_list = []
while i < n:
    if array[i] < 0:
        neg = neg+1
        neg_list.append(array[i])
    i = i+1

print('Array = {}'.format(array))
print('Total Negative numbers = {}'.format(neg))
print('List of Negative Numbers = {}'.format(neg_list))

#end