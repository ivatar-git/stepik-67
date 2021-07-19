sum, pow = 0, 0
while True: #бесконечный цикл
    a = int(input())
    sum += a #суммируем input
    pow += a ** 2 #суммируем квадраты input
    if sum == 0: #разрываем цикл
        break
print (pow)
