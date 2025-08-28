"""
B. Простая сортировка
ограничение по времени на тест 2 секунды
ограничение по памяти на тест 64 мегабайта
Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные
В первой строке входного файла содержится число N (1≤N≤100_000) — количество элементов в массиве.
Во второй строке находятся N целых чисел, по модулю не превосходящих 10^9.

Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания, между любыми двумя
числами должен стоять ровно один пробел


Входные данные
10
1 8 2 1 4 7 3 2 3 6

Выходные данные
1 1 2 2 3 3 4 6 7 8
"""

import random


def sort_quick(array):
    if len(array) <= 1:
        return array
    size = len(array)
    pivot_index = random.randint(0, size - 1)
    pivot_element = array[pivot_index]
    left = [item for item in array if item < pivot_element]
    middle = [item for item in array if item == pivot_element]
    right = [item for item in array if item > pivot_element]
    return sort_quick(left) + middle + sort_quick(right)


def main():
    n = int(input().strip())
    array = list(map(int, input().split()))
    result = sort_quick(array)
    print(*result)


if __name__ == "__main__":
    main()
