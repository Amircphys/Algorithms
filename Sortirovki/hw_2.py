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


def merge(left_array, right_array):
    L = len(left_array)
    R = len(right_array)
    result = [None for _ in range(L + R)]
    i, j = 0, 0
    while i + j < L + R:
        if j == R or (i < L and left_array[i] < right_array[j]):
            result[i + j] = left_array[i]
            i += 1
        else:
            result[i + j] = right_array[j]
            j += 1
    return result


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    left_array = [array[i] for i in range(n // 2)]
    right_array = [array[i] for i in range(n // 2, n)]
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    return merge(left_array, right_array)


def main():
    n = int(input().strip())
    array = list(map(int, input().split()))
    result = merge_sort(array)
    print(*result)


if __name__ == "__main__":
    main()
