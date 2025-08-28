"""
Дан небольшой массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные
В первой строке входного файла содержится число n (1≤n≤1000) — количество элементов в массиве.
Во второй строке находятся n целых чисел, по модулю не превосходящих 10^9.

Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания,
между любыми двумя числами должен стоять ровно один пробел.

Входные данные:
10
1 8 2 1 4 7 3 2 3 6
Выходные данные
1 1 2 2 3 3 4 6 7 8
"""


def sort_bubble(array):
    J = len(array)
    while J > 1:
        for i in range(1, J):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        J -= 1
    return array


def sort_insert(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def sort_selection(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
    return array


def sort_cocktail_shaker(array):
    left, right = 0, len(array) - 1
    while left < right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    return array


def main():
    n = int(input().strip())
    array = list(map(int, input().split()))
    result = sort_cocktail_shaker(array)
    print(*result)


if __name__ == "__main__":
    main()
