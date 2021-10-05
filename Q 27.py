# string="raziya"
# list=[]
# i=0
# while i<len(string):
#     list.append(string[i])
#     i=i+1
# print(list)
# # list.remove(list[0])
# # list.remove(list[5])
# list.insert(list[0],"a")
# list.insert(list[5],"r")
# print(list)

string=input("enter the string :")
list=[]
i=0
while i<len(string):
    list.append(string[i])
    i=i+1
print(list)
j=len(list)-1
list2=[]
while j>=0:
    list2.append(list[j])
    j=j-1
print(list2)
if list==list2:
    print("it is palindrome")
else:
    print("it is not palindrome")