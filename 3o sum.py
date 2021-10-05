number=30
n=[10,11,12,13,14,17,18,19]
b=[]
i=0
while i<(len(n)/2):
    j=0
    while j<len(n):
        num=n[i]+n[j]
        if number==num:
            k=n[i]
            l=n[j]
            b.append([k,l])
        j=j+1
    i=i+1
print(b)


b=[]
for i in range (len(n)/2):
    for j in range (len (n)):
        num=n[i]+n[j]
        if number==num:
            k=n[i]
            l=n[j]
            b.append([k,l])
print(b)