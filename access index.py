num=int(input("enter the number of item : "))
i=0
a=[]
while i<num:
    num1=int(input("enter the number : "))
    a.append(num1)
    i=i+1
print(a)
x=0
while x<(len(a)):
    y=a[x]
    print("index value of",x,"=",y)
    x=x+1