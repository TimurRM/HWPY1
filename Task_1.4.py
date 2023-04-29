# Задача 4. Напишите программу, которая на вход принимает число (N), а 
# на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def find_even_numbers(n):
    even_numbers = []
    for i in range(2, n+1, 2):
        even_numbers.append(i)
    return even_numbers


n = int(input("Введите число: "))
even_numbers = find_even_numbers(n)
print(even_numbers)

