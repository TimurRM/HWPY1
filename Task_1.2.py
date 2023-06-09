# Задача 2. Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21.   


def distance_between_points(x1, y1, x2, y2):
    
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

x1 = float(input("Введите координату x первой точки: "))
y1 = float(input("Введите координату y первой точки: "))
x2 = float(input("Введите координату x второй точки: "))
y2 = float(input("Введите координату y второй точки: "))
    
distance_AB = distance_between_points(x1, y1, x2, y2)
print(f"Расстояние между точками A{x1,y1} и B{x2,y2} равно {distance_AB:.2f}")

