# Given start and end of a range, write a Python program to print 
# all positive numbers in given range.
# Example:
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 

# Input: start = -3, end = 4
# Output: 0, 1, 2, 3, 4

start=int(input("enter the number"))
end=int(input("enter the number"))
i=start
while i<=end:
    if i>0:
        print(i)
    i=i+1