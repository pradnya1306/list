number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<(len(number)):
    if number[i]>max:
        max=number[i]
    i=i+1
print("1st max number",max)
number.remove(max)
print(number)
max=0
for i in range(len(number)):
    if number[i]>max:
        max=number[i]
print("2nd max number",max)