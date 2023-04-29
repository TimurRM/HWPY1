# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def get_quarter_range(quarter_num):
    if quarter_num == 1:
        x_range = "x > 0"
        y_range = "y > 0"
    elif quarter_num == 2:
        x_range = "x < 0"
        y_range = "y > 0"
    elif quarter_num == 3:
        x_range = "x < 0"
        y_range = "y < 0"
    elif quarter_num == 4:
        x_range = "x > 0"
        y_range = "y < 0"
    else:
        return "Номер четверти должен быть от 1 до 4"

    return f"Диапазон координат точек в {quarter_num} четверти: {x_range}, {y_range}"

quarter_num = int(input("Введите номер четверти (1-4): "))
quarter_range = get_quarter_range(quarter_num)
print(quarter_range)
