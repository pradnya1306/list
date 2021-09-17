list=[2,4,3,1,6]
i=0
a=[]
while i<len(list):
    if i%2==0:
        a.append(list[i])
    else:
        list.sort()
print(list)