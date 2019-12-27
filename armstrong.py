n=f=int(input('Enter Number : '))
c=10
k=0
i=1
d=10
s=0
j=0
while f%d!=f:
    i=i+1
    d=d*c        
#print(i, 'digit number')

while j<i:
    a=n%c
    s=s+(a**i)
    n=int(n/c)
    j=j+1      
            
if s==f:
    print('Armstrong Number')
else:
    print('Not an Armstrong number')

    
