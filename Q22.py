a=[1,2,[1,2,3],4,5,[6,5]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            # print(j)
            j=j+1
    else:
        
        sum=sum+a[i]    
    i=i+1
print(sum)

# for i in range(len(a)):
#     if type(a[i])==list:
#         for j in range(len(a[i])):
#             sum=sum+a[i][j]
#     else:
#         sum=sum+a[i]
# print(sum)

