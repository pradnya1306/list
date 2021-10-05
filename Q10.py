#  Remove empty List from List        
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

list=[5, 6, [], 3, [], 9]
i=0
while i<len(list):
    if list[i]==[]:
        list.remove(list[i])
    
    i=i+1
print(list)