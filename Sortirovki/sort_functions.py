# Сортировка вставками
def sort_by_insert(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


# Сортировка пузырьковая
def sort_bubble(array):
    J = len(array)
    while J > 1:
        for i in range(1, J):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        J -= 1
    return array


# Сортировка выбором
def sort_selection(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# Сортировка слиянием
def merge(array_left, array_right):
    result = [None for _ in range(len(array_left) + len(array_right))]
    i, j = 0, 0
    while i + j < len(array_left) + len(array_right):
        if j == len(array_right) or (
            i < len(array_left) and array_left[i] < array_right[j]
        ):
            result[i + j] = array_left[i]
            i += 1
        else:
            result[i + j] = array_right[j]
            j += 1
    return result


def sort_merge(array):
    n = len(array)
    if n <= 1:
        return array
    left_array = [array[i] for i in range(n // 2)]
    right_array = [array[i] for i in range(n // 2, n)]
    left_array = sort_merge(left_array)
    right_array = sort_merge(right_array)
    return merge(left_array, right_array)


# Быстрая сортировка
def sort_quick(array):
    if len(array) <= 1:
        return array
    pivot_element = array[len(array) // 2]
    left_array = [element for element in array if element < pivot_element]
    middle_array = [element for element in array if element == pivot_element]
    right_array = [element for element in array if element > pivot_element]
    return sort_quick(left_array) + middle_array + sort_quick(right_array)
