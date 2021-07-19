lst = [int(i) for i in input().split()]
x = int(input())
c = 0
for i in range(len(lst)):
    if x not in lst:
        print('Отсутствует')
        break
    if x == lst[i]:
        print(c,' ', end='')
        c += 1
    else:
        c += 1