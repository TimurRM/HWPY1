# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение


def get_day_name(day_number):
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }

    if not day_number:
        return "До свидания!" 
    elif day_number in days:
        return f'{day_number} -> {days[day_number]}'
    else:
        return f'{day_number} -> "Нет такого дня"'

while True:
    try:
        day_number = int(input("Введите номер дня недели (или 0, чтобы выйти): "))
        day_name = get_day_name(day_number)
        print(day_name)
        if day_name == "До свидания!":
            break
    except ValueError:
        print("Ошибка ввода! Введите целое число.")


