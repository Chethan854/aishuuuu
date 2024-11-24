import math
p=3
q=7
n=p*q
print("n=",n)
phi=(p-1)*(q-1)
print("phi=",phi)
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e+=1
print("e=",e
k=2
d=(1+(k*phi))/e
print