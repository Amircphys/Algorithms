"""
Ваша задача - проверить, содержит ли данная последовательность элемент, который встречается более половины раз.
Выведите 1, если в последовательности содержится элемент, который встречается больше, чем n/2 раз, и  0 в противном случае.
"""


def search_major_element(arr: list[int]) -> int:

    if not arr:
        return 0
    temp_item = arr[0]
    temp_count = 0
    for i in range(len(arr)):
        if arr[i] == temp_item:
            temp_count += 1
        else:
            temp_count -= 1
            if temp_count == 0:
                temp_item = arr[i]
                temp_count = 1

    cnt = 0
    for item in arr:
        if item == temp_item:
            cnt += 1
    if cnt > len(arr) // 2:
        return 1

    return 0


print(search_major_element([1, 2, 2, 3, 2]))
