
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
sum2=0
count=0
count1=0
count2=0
while i<len(elements):
    count=count+1
    sum=sum+elements[i]
    if elements[i]%2==0:
        sum1=sum1+elements[i]
        count1=count1+1
    else:
        sum2=sum2+elements[i]
        count2=count2+1
    i=i+1
print("count of all number",count)
print("count of even number",count1)
print("count of odd number",count2)
print("sum of all number",sum)
print("sum of evev number ",sum1)
print("sum of odd number",sum2)
average1=sum//count
average2=sum1//count1
average3=sum2//count2
print("average of allnumber",average1)
print("average of even number",average2)
print("average of odd number",average3)

# for i in range(len(elements)):
#     count=count+1
#     sum=sum+elements[i]
#     if elements[i]%2==0:
#         sum1=sum1+elements[i]
#         count1=count1+1
#     else:
#         sum2=sum2+1
#         count2=count2+1
# print("count of all number",count)
# print("count of even number",count1)
# print("count of odd number",count2)
# print("sum of all number",sum)
# print("sum of evev number ",sum1)
# print("sum of odd number",sum2)
# average1=sum//count
# average2=sum1//count1
# average3=sum2//count2
# print("average of allnumber",average1)
# print("average of even number",average2)
# print("average of odd number",average3)
