number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(number):
    if number[i]>max:
        max=number[i]
    i=i+1
print("max number is",max)
# number.remove(max)
number.sort()
print(number)
print("second largest number",number[-2])
# j=0
# second_max=0
# while j<len(number):
#     if number[j]>second_max:
#         second_max=number[j]
#     j=j+1
# print("second max number is",second_max)

        
