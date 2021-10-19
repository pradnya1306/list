a=[[1,2,3,4],[5,4,3,3]]
i=0
m=[]
while i<len(a)-1:
    j=0
    while j<len(a[i]):
        k=a[i][j]*a[i+1][j]
        # print(k)
        m.append(k)
        j=j+1
    i=i+1
print(m)