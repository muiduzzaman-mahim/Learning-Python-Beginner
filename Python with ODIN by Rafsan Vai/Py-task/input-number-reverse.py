#start program  
     
Num = int(input("Please Enter a Number to reverse: \n"))    
Rev = 0    

while(Num == 0):    
    Rem = Num % 10    
    Rev = (Rev * 10) + Rem  
    Num = Num // 10   
     
print("\nReversed = %d" %Rev) 

#end program