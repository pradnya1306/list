# Write a Python program to convert a given list of strings into list of lists. 
# Originallist of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], 
# ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
strings=['Red', 'Maroon', 'Yellow','olive']

# main_list=[]

# b=list(a)
i=0
main_list=[]
while i<len(strings):
    b=list(strings[i])
    main_list.append(b)
    i=i+1
print(main_list)
