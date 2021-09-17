# num=int(input("enter the number"))
# i=0
# element=[]
# while i<num:
#     num1=int(input("enter the element"))
#     element.append(num1)
#     i=i+1
# print(element)

element=[23,14,56,12,19,9,15,25,31,42,43]

m=0
count=0
count1=0
while m<len(element):
    if element[m]%2==0:
        count=count+1  
        
    else:
        count1=count1+1
        
    m=m+1
print("even number is",count)
print("odd number is",count1)