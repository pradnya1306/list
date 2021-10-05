# Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

list = [1,2,3,1,2,2]
i=0
a=[]
while i<len(list):
    j=0
    count=0
    while j<len(list):
        if list[i]==list[j]:
            if list[i] not in a:
                a.append(list[i])
    
        j=j+1
    
    i=i+1
print(a)
