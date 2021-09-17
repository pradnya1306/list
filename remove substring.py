mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."

subStr = "over"
i=0
a=[]
while i<len(mainStr):
    if i=="over":
        continue
    a.append(mainStr)
print(a)
# for i in mainStr:
#     if i== "over":
#         print( )
#     else:
#         continue
# print(mainStr)