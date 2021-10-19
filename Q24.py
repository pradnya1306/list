list=[1,3,5,7,9,16]
i=0
list2=[]
while i<len(list)-1:
    sub=list[i+1]
    sub=sub-list[i]
    list2.append(sub)
    i=i+1
print(list2)
