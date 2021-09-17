magic_square = [[8, 3, 4],    
                [1, 5, 9],
                [6, 7, 1]]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum=sum+magic_square[i][j]
        j=j+1
    print("row",i+1,sum)


    m=0
    sum1=0
    while m<len(magic_square):
        sum1=sum1+magic_square[m][i]
        m=m+1
    print("coulmn",i+1,sum1)
    
    i=i+1


n=0
sum2=0
while n<len(magic_square):
    sum2=sum2+magic_square[n][n]
    n=n+1
print("diagnolal 1 ",sum2)

k=0
sum3=0
while k<len(magic_square):
    p=(len(magic_square)-1)-k
    # sum3=0
    while p<(len(magic_square)-k):
        sum3=sum3+magic_square[k][p]
        p=p+1
    
    # print("diagnolal 2",sum3)

    k=k+1
print("diagnolal 2",sum3)
if sum==sum1==sum2==sum3:
    print("its magic square")
else:
    print("its not magic square")
