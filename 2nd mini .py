a=[167,12,13,14,9]
mini=a[0]
for i in range(len(a)):
    if a[i]<mini:
        mini=a[i]
print("1st mini number",mini)
a.remove(mini)
print(a)
mini=a[0]
for i in range(len(a)):
    if a[i]<mini:
        mini=a[i]
print("2nd mini number",mini)
