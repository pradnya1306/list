number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
length=len(number)
while i<length:
    if number[i]>max:
        max=number[i]
    i=i+1
print(max)