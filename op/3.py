"# -- coding: utf-8 --"
name=input("Имя ")
age=int(input("Возраст "))
if 16<=age<75:
    if name != "Иван":
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Вы не поступили в ВГУИТ")
else:
    print("Вам осталось учиться в школе: ", 16-age, " лет")