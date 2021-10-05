a=[[1,2,3],[4,5,6]]
i=0
list1=[]
list2=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            list1.append(a[i][j])
        else:
            list2.append(a[i][j])
        j=j+1

    i=i+1
print(list1)
print(list2)