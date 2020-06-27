list1=list()
list2=list()
while(True):
  x=input("Enter STOP or number: ")
  if(x=='STOP'):
      break
  x=int(x)
  list1.append(x)
#print(list1)
for i in list1:
    if i>0:
        list2.append(i)
print("Positive numbers are:",list2)
