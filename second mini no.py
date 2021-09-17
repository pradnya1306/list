a=[167,12,13,14,9]
m=0
mini=a[0]
b=[]
while m<len(a):
    if a[m]<mini:
        mini=a[m]
    m=m+1
# print(mini)
a.remove(mini)
n=0
mini1=a[0]
b=[]
while n<len(a):
    if a[n]<mini1:
        mini1=a[n]
    n=n+1
print("second mini number is",mini1)

