# Given the start and end of a range, write a Python program to print all negative numbers in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# Input: start = -3, end = 4
# Output: -3, -2, -1
start=int(input("enter the number"))
end=int(input("enter the number"))
i=start
while i<=end:
    if i<0:
        print(i)
    i=i+1
