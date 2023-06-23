"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

n = int(input("Введите длину массива: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите значение в массив: ")))
x = int(input("Введите число которое хотите найти в массиве: "))

flag = False
for i in range(n):
    if lst[i] == x:
        print("Самое близкое число: ", lst[i])
        flag = True

if not flag:
    closest_lst = lst[0]
    min_diff = abs(closest_lst - x)

    for elem in lst:
        diff = abs(elem - x)
        if diff < min_diff:
            closest_lst = elem
            min_diff = diff
    print("Самое близкое число: ", closest_lst)

