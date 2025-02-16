#bank.py
#Week 2 Task - Prompt user to input 2 amounts in cents add the amounts together and print out in readable format
#Author: Lorraine Morrissey

amount1 = int(input("Enter amount1(in cents): "))
amount2 = int(input("Enter amount2(in cents):"))
totalamount = ((amount1 + amount2)/100)
print ("The sum of these is €"+ f"{totalamount}")