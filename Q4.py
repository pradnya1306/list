# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])



originallist=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 1]]
i=0
maxlen=0
maxlist=[]
while i<len(originallist):
    if len(originallist[i])>maxlen:
        maxlen=len(originallist[i])
        maxlist=(originallist[i])
    # print(maxlen,originallist[i])  
    i=i+1
print(maxlen,maxlist) 

# count=0
# for i in originallist:
#     le
#     count=count+1[]
    
# print(count)


    
