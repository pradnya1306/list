a=[1,2,3,4,5,6,7,8,9,10]
length=int(input("enter the number from reverse "))
i=len(a)-1
b=[]
while i>=length:
    b.append(a[i])
    i=i-1
print(b)