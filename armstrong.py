n=f=int(input('Enter Number : '))
k=0
s=0
j=0
i=len(str(n))
#print(i, 'digit number')

while j<i:
    a=n%10
    s=s+(a**i)
    n=int(n/10)
    j=j+1      
            
if s==f:
    print('Armstrong Number')
else:
    print('Not an Armstrong number')

    
