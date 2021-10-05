a=[5,6,7,8,3,2,1,5]
i=0
while i<len(a):
    a.pop(i)
    i=i+1
print(a)

a=[3,4,6,2,1,6,5]
i=0
b=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    i=i+1
print(b)

m=[1,2,3,4,5,6,7,8,9,]
i=0
b=[]
while i<len(m):
    if m[i]%2:
       b.append(20)
    #    i=i+1
    else:
        b.append(m[i])
    i=i+1
print(b)

# i=0
# while i<len (m):
#     if i!=0:
#         m.insert(i,20)
#     i=i+2

# print(m)









# i=0
# n=[]
# while i<len(m):
#     if i!=0:
#         if i%2==0:
#             n.insert(i,20)
#         else:
#             n.append(m[i])
#     i=i+1
# print(n)    