sum = 0
pow = 0
while True:
    a = int(input())
    sum += a

    if sum == 0:
        print(pow + a ** 2)
        break

    else:
        pow += a ** 2