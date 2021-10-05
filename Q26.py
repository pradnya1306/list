a=[1,2,3]
i=0
list1=[]

while i<len(a):
    
    j=0
    while j<len(a):
        p=[a[i],a[j]]
        list1.append(p)
        n=0
        while n<len(a):
            m=[a[i],a[j],a[n]]
            list1.append(m)
            n=n+1
        j=j+1
    i=i+1
print(list1)

