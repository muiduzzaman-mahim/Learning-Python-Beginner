#convert 

v = 'I love Bangladesh'
result = ' '

for i in v:
    if i == 'a' or i == 'e' or i == 'i' or i == 'u' or  i == 'o' or i == 'A' or i == 'E' or i == 'O' or i == 'I' or i == 'U':
        result = result + i.upper()
    else:
        result = result + i

print(result)