#### Collatz Sequence ####

import sys
#Collatz function Definition
def collatz(number):
    if(number%2==0):
        number=number//2
        return number
    elif (number%2==1):
        number = (3*number)+1
        return number

print("Enter A Number")
intNumber=int(input()) ## Taking input number
print(intNumber,end=',')

while(True):
    intNumber=collatz(intNumber) # Calling Function returns a number depending upon even or odd
    if(intNumber==1):
        print(intNumber)
        break;
    else:
        print(intNumber, end=',')
        continue;

sys.exit()    
