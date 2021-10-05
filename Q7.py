# list=[2,4,3,1,6]
list=[10,4,3,8,1]
i=0
b=[]
while i<len(list):
    if list[i]%2!=0:
        b.append(list[i])
    i=i+1
# print(list)
b.sort()
print(b)