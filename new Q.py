string="567895"
i=0
list1=[]
while i<(len(string)-1):
    
    n=string[i]+string[i+1]
    list1.append(int(n))
    i=i+1
print(list1)
max=0
for j in range(len(list1)):
    if(list1[j])>max:
        max=list1[j]
print(max)

