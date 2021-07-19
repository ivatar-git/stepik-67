list = [int(i) for i in input().split()]
newlist = []
for i in list:
    if list.count(i) > 1:
        newlist.append(i)
print(*set(newlist))