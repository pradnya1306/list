# num=int(input("enter the number of item :"))
# i=0
# a=[]
# while i<num:
#     num1=int(input("enter the number : "))
#     a.append(num1)
#     i+=1
# print(a)
a=[1,12,13,14,9]
x=0
mini=a[0]
while x<(len(a)):
    if a[x]<mini:
        mini=a[x]
    x+=1
print(mini)
