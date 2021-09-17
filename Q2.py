# Convert Character Matrix to single String;
#     The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest
list = [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
while i<len(list):
    j=0
    join=[]
    while j<len(list[i]):
        print(list[i][j],end="")
        j=j+1
    i=i+1
        
