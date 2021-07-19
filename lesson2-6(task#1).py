sum = 0 #переменная для суммы input
pow = 0 #переменная суммы квадратов input
while True: #бесконечный цикл
    a = int(input())
    sum += a #суммируем input

    if sum == 0: #печатаем накопленный pow и разрываем цикл
        print(pow + a ** 2)
        break

    else: #суммируем pow
        pow += a ** 2