# Write a Python program to sum two or more lists, the lengths of the 
# lists may be different. 
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]
list=[[1, 2, 4],
 [2, 4, 4], 
 [1, 2]]
i=0
sum=0
while i<len(list):
    j=0
    while j<len(list):
        sum=sum+list[j][i]
        j=j+1
        print(sum)
    i=i+1
print(sum)