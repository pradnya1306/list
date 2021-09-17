elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
m=0
sum=0
sum1=0
count=0
count1=0
while m<len(elements):
    if elements[m]%2==0:
        sum=sum+elements[m]
        count=count+1
    else:
        sum1=sum1+elements[m]
        count1=count1+1
    m=m+1    
average=sum//count
average1=sum1//count1
print("even number",average)
print("odd number",average1)
