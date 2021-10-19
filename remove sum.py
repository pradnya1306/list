a=[[2,5,7,8],[4,3,7,6]]
i=0
d=[]
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]%2==0:
            d.append(a[i][j])
        else:
            c.append(a[i][j])
        j=j+1
    i=i+1
print(d)
print(c)
