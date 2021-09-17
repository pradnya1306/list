# Write a Python program to create a list reflecting the modified run-length encoding from 
# a given list of integers or a given list of characters. 
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
from os import posix_fadvise


Originallist=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
a=[]
while i<len(Originallist):
    j=0
    count=0
    b=[]
    while i<len(Originallist):
        if Originallist[i]==Originallist[j]:
            count=count+1
    
        j=j+1
        b.append(count)
        b.append(Originallist[i])
        if b not in a:
            a.append(count)
        else:
            a.append(b)
        

    i=i+1
print(a)

        
