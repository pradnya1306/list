name=input("enter the name")
i=0
a=[]
while i<len(name):
    a.append(name[i])
    i=i+1
print(a)
j=0
while j<len(a):
    if a[j] in('a,e,i,o,u'):
        print(a[j],"is vowel.")
    else:
        print(a[j],"is consonent.")
    j=j+1
