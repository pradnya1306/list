name=input("enter the name : ")
name2=list(name)
# name2.sort()
# print(name2)
i=0
k=[]
m=[]
while i<len(name2):
    if name2[i]in("a","i","e","o","u"):
        k.append(name2[i])
        # print(name2[i],"vowels")
    else:
        m.append(name2[i])
        # print(name2[i],"component")
    i=i+1
print(k)
print(m)
