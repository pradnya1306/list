# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22

input=[4, 5, 5, 5, 3, 8]
# input= [1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
a=[]
while i<len(input):
    j=0
    count=0
    
    while j<len(input):
        if input[i]==input[j]:
            count=count+1
            if count==3:
                if input[i] not in a:
                    a.append(input[i])
        j=j+1
                 
    i=i+1
print(a)
