# print count between 20 to 40
num=[50,40,23,70,56,12,5,10,7]
# length=len(num)
# index=0
# less_than40=0
# more_than20=0
# while index<length:
#     number=num[index]
#     if number<40:
#         less_than40=less_than40+1
#     else:
#         more_than20=more_than20+1
#     index+=1
# print("less_than 40=",(str(less_than40)))
# print("more_than 20=",(str(more_than20)))

i=0
count=0
length=len(num)
while i<length:
    if num[i]>=20 and num[i]<=40:
        count=count+1
    i=i+1
print(count)
