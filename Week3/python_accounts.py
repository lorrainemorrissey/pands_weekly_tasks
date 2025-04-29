# python_accounts.py
# Week 3 Task - Prompt user to input 10 character account number and output in the below format 
# output format - (first digits replaced with X followed by last 4 digits of account number)
#Author: Lorraine Morrissey

accno = str(input("Please enter your 10 digit Account number: "))
#print (f"Your account number is {accno}")

# Get length of the string
accno_length = len(accno)

# Get last 4 digits
endno = accno_length-4

Last4digits = accno[endno:]
print ("Your account number is ******{}".format(Last4digits))