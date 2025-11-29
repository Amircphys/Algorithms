"""
Ваша задача - проверить, содержит ли данная последовательность элемент, который встречается более половины раз.
Выведите 1, если в последовательности содержится элемент, который встречается больше, чем n/4 раз, и  0 в противном случае.
"""


def search_quarter_element(arr):
    counts = [0 for _ in range(3)]
    elements = [None for _ in range(3)]
    found = False
    for temp_element in arr:
        for i, element in enumerate(elements):
            if element == temp_element:
                counts[i] += 1
                found = True
                break
        if found:
            continue

        for i in range(3):
            if counts[i] == 0:
                elements[i] = temp_element
                counts[i] = 1
                found = True
                break
        if found:
            continue

        for i in range(3):
            counts[i] -= 1

    for candidate in elements:
        temp_cnt = 0
        for item in arr:
            if item == candidate:
                temp_cnt += 1
        if temp_cnt < len(arr) // 4:
            print(candidate)
            return 0
    return 1


print(search_quarter_element([0, 9, 2, 3, 9, 0, 2, 9, 2, 3, 3]))
