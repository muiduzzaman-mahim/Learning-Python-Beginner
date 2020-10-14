#start program  
     
Num = int(input("Please Enter a Number to check palindrome: \n"))    
temp = Num
Rev = 0    

while(Num > 0):    
    Rem = Num % 10    
    Rev = (Rev * 10) + Rem  
    Num = Num // 10            
print("\nReverse form of this number = %d\n" %Rev) 

if temp == Rev:
    print('so, {} is a palindrome number\n'.format(temp))
else:
    print('so, {} is not a palindrome number\n'.format(temp))

#end program