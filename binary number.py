# binary_number=[1,0,0,1,1,0,1,1]
num=int(input("enter the number of item"))
i=0
binary_number=[]
while i<num:
    item=int(input("enter the number"))
    binary_number.append(item)
    i=i+1
print(binary_number)
i=0
length=len(binary_number)
a=[]
while i<length:
    length=length-1
    a.append(binary_number[length])
print(a)
j=0
sum=0
length=len(a)
while j<length:
    n=2**j*a[j]
    sum=sum+n
    j=j+1
print(sum)
