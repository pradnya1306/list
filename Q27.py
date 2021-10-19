# a=[5,6,7,8,3,2,1,5]
# i=0
# while i<len(a):
#     a.pop(i)
#     i=i+1
# print(a)

# a=[3,4,6,2,1,6,5]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     i=i+1
# print(b)

# m=[1,2,3,4,5,6,7,8,9,]
# i=0
# b=[]
# while i<len(m):
#     if m[i]%2:
#        b.append(20)
#     #    i=i+1
#     else:
#         b.append(m[i])
#     i=i+1
# print(b)


# M=[1,2,3,4,5,6,7,8]
# i=0
# while i<len (m):
#     if i!=0:
#         m.insert(i,20)
#     i=i+2

# print(m)






a=[1,2,3,[4,5,6]]  
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j <len(a[i]):
            b.append(a[i][j])
            
            j=j+1
    else:
        b.append(a[i])
        
    i=i+1
print(b)