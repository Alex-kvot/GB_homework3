"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

n = int(input("Введите длину массива: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите значение в массив: ")))
x = int(input("Введите число которое хотите найти в массиве: "))

k = 0
for i in range(n):
    if lst[i] == x:
        k += 1
print("Сколько раз число ", x, " встречается в массиве: ", k)
