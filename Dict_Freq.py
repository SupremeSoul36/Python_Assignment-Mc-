#most-frequently
def most_frequent(str):
    d=dict()
    l=list()
    for x in str:
        d[x]=d.get(x,0)+1
    for k,v in d.items():
        new=(v,k)
        l.append(new)
    l=sorted(l,reverse=True)
    return l

str=input('Enter a string: ')
l=most_frequent(str)
for k,v in l:
    print(v,'=',k)
