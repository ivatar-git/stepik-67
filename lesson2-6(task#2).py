a = int(input())
list = []
for i in range(1, a+1):
    list += ([str(i)] * i)
print(*list[:a])
