newlist = []

for i in range(1, 21):
    newlist.append(i)

print("List -", newlist)

"""
for i in newlist:
    if(i == 3):
        break
    print(i , "inside of the loop")

print(i ,"outside of the loop")
"""

for i in newlist:
    if i == 3:
        continue
    print(i, "inside of the loop")
