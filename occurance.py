# char_list = ["a","n","t","a","a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
char_list=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
a=[]
count=0
while i<len(char_list):
    j=0
    b=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
            
        j=j+1
    b.append(char_list[i])  
    b.append(count)
    if b not in a:
        a.append(b)
    i=i+1
print(a)


    
