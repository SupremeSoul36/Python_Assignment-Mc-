n=input("Enter number of fibonacci terms:")
n=int(n)
m=n
l=list()
a=0
b=1
if n>0:
    l.append(a)
if n>1:
    l.append(b)

while(n-2>0):
    c=a+b
    l.append(c)
    a=b
    b=c
    n=n-1
print("First",m,"fibonacci are: \n",l)
