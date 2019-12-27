"""n=f=int(input('Enter Number : '))"""
n=f=o=0
c=10
k=0
while f<10000000000:
    i=len(str(f))
    j=0
    s=0
    #print(i, 'digit number')
    

    while j<i:
            a=n%c
            s=s+(a**i)
            n=int(n/c)
            j=j+1
            
    k=k+1
    n=o=0+k
            
    if s==f:
            print(f)
    f=f+1
    
