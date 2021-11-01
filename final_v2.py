#coding=utf8

import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class My_window:
    def __init__(self, main):
        self.main = main
        self.main.title('webcam')
        # переменная brightness для контроля яркости
        self.brightness = 0
        # поле для ввода названия скриншота со значением по умолчанию
        self.entry = Entry(self.main, width=46)
        self.entry.insert(0, "my_screenshot")
        self.entry.grid(row=6, column=0, )
        # кнопка сохранения кадра
        self.save_button = Button(self.main, text="Сохранить кадр", command=self.save_frame, height=1, width=20,
                                  activeforeground='red')
        self.save_button.grid(row=6, column=2)
        # кнопка закрытия программы
        self.close_button = Button(self.main, text="Закрыть", command=self.close, height=1, width=20,
                                   activeforeground='red')
        self.close_button.grid(row=5, column=2)
        # слайдер
        self.brightness_slider = Scale(self.main, from_=-150, to=150, command=self.print_scale_value, label='Яркость:',
                                       variable=self.brightness, orient=HORIZONTAL, length=280)
        self.brightness_slider.set(0)
        self.brightness_slider.grid(row=5, column=0)
        # переменная cap, предполагаем использовать камеру 0
        self.cap = cv2.VideoCapture(0)
        # запускаем бесконечный цикл update
        self.update()

    # функция получает кадр из функции get_frame каждые x ms и конвертирует из формата cv2
    def update(self):
        ret, frame = self.get_frame()
        self.image = Image.fromarray(frame)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.main, height=480, width=600, bg='white')
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=0, rowspan=3, columnspan=4)
        self.main.after(50, self.update)

    # функция получает кадр из камеры, изменяет яркость и конвертирует BGR>RGB
    def get_frame(self):
        ret, frame = self.cap.read()

        frame = cv2.flip(frame, 1)  # зеркалим кадр по горизонтали для удобства

        ##магия с brightness обработкой в hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_int16 = hsv.astype(np.int16)
        hsv_int16[:, :, 2] += self.brightness_slider.get()
        hsv_int16_clip = np.clip(hsv_int16, 0, 255)
        hsv_uint8 = hsv_int16_clip.astype(np.uint8)
        frame = cv2.cvtColor(hsv_uint8, cv2.COLOR_HSV2BGR)
        ##магия всё

        return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # функция сохраняет скриншот
    def save_frame(self):
        # получаем желаемое имя файла из entry поля
        filename = self.entry.get()
        # проверяем, что желаемое имя файла не пустое или не забито пробелами (strip)
        if len(filename.strip()) == 0:  # если проверка не пройдена - подсказка
            return messagebox.showinfo('Внимание', 'Укажите имя файла перед сохранением кадра. Спасибо-пожалуйста!')
        # если всё ок - сохраняем кадр с камеры
        else:
            ret, frame = self.get_frame()
            self.filename = self.entry.get()
            cv2.imwrite(self.filename + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    # функция уничтожает окно main закрывая программу
    def close(self):
        self.main.destroy()

    # callback для слайдера
    def print_scale_value(self, new):
        # print("Значение brightness:", new)
        pass


def main():
    root = Tk()
    root.geometry("600x600")
    GUI = My_window(root)
    root.mainloop()
    print("Закрываем программу")


main()
