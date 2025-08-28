"""
C. Количество инверсий
ограничение по времени на тест 5 секунд
ограничение по памяти на тест 256 мегабайт
Напишите программу, которая для заданного массива A=⟨a1,a2,…,an⟩ находит количество пар (i,j) таких, что i<j и ai>aj.

Входные данные
Первая строка входного файла содержит натуральное число n (1≤n≤500000) — количество элементов массива.
Вторая строка содержит n попарно различных элементов массива A (0≤ai≤10^6).

Выходные данные
В выходной файл выведите одно число — ответ на задачу.

Примеры

Входные данные
4
1 2 4 5
Выходные данные
0

Входные данные
4
5 4 2 1
Выходные данные
6
"""

K = 0


def merge(left_array, right_array):
    global K
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
            K += L - i
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
    print(K)


if __name__ == "__main__":
    main()
