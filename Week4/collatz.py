# collatz.py
# Week 4 Task -  input a positive integer. If ever

#Author: Lorraine Morrissey

# Input integer
num = int (input('Please enter a positive integer: '))
print (num, sep=" ", end=" ")

while (num != 1):
    
    if (num % 2) == 0:
        num = int(num/2)
        print (num, sep=" ", end=" ")
    else:  
        num = int(num*3)+1
        print (num, sep=" ", end=" ")