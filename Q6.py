# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectively.


# n= [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
n= [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
i=0
a=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            count=count+1
            if count>=2:
                if n[i]not in a:
                    a.append(n[i])
        j=j+1
    i=i+1
print(a)
