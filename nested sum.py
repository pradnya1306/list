a=[[1,2,3],[4,5,6],[6,7,8]]
i=0
while i<len(a)-1:
    
    j=0
    while j<len(a[i]):
        sum=a[i][j]+a[i+1][j]
        print(sum)
        j=j+1
    i=i+1

# i=0
# while i<10:
#     if i%2==0:
#         print(i**2)
#     else:
#         print(-i)
#     i=i+1

# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# i=0
# while i <len(a):
#     print(a[i],b[-(i+1)])
#     i=i+1

# a="pradnya"
# b=list(a)
# i=len(b)-1
# c=[]
# while i>=0:
#     c.append(b[i])
#     i=i-1
# print(c)
# print("".join(c))


    
