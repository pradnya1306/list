a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
i=0
while i<len(a):
    if i!=0:
        if i%3==0:
            a.insert(i,20)
        i=i+1
print(a)