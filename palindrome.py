
# name=['n','i','t','i','n']
# i=0
# length=len(name)
# a=[]
# while i<length:
#     length=length-1
#     a.append(name[length])
# print(a)
# if a==name:
#     print("palindrome list")
# else:
#     print("not palindrome list")







# i=len(name)-1
# a=[]
# while i>=0:
#     num=(name[i])
#     a.append(num)
#     i-=1
# print(a)
# if a==name:
#     print('palindrome')
# else:
#     print("not palindrome")


num=int(input("enter the number of item : "))
i=0
a=[]
while i<num:
    num1=int(input("enter the number : "))
    a.append(num1)
    i=i+1
print(a)
x=len(a)-1
b=[]
while x>=0:
    z=a[x]
    b.append(z)
    x=x-1
print(b)
if a==b:
    print("palindrome")
else:
    print("not palindrome")

