# mark=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# mark = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
mark = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
i=0

while i<len(mark):
    j=0
    sum=0
    while j<len(mark[i]):
        sum=sum+(mark[i][j])
        j=j+1
    average=sum//len(mark[i])
    print("Average of",i+1,"year",average)
    i=i+1