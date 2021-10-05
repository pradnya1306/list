n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11,5]
# n=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
a=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            count=count+1
            if count>=2:
                if n[i]not in a:
                    a.append(n[i])
        j=j+1
    i=i+1
print(a)

