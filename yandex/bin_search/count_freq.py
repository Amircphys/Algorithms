def bin_search_left(array, x):
    result = -1
    left_idx, right_idx = 0, len(array) - 1
    while right_idx >= left_idx:
        middle_idx = (left_idx + right_idx) // 2
        middle_item = array[middle_idx]
        if middle_item == x:
            result = middle_idx
            right_idx = middle_idx - 1
        elif middle_item > x:
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return result


def bin_search_right(array, x):
    result = -1
    left_idx, right_idx = 0, len(array) - 1
    while right_idx >= left_idx:
        middle_idx = (left_idx + right_idx) // 2
        middle_item = array[middle_idx]
        if middle_item == x:
            result = middle_idx
            left_idx = middle_idx + 1
        elif middle_item > x:
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return result


def count_freq(array, x):
    left_idx = bin_search_left(array, x)
    right_idx = bin_search_right(array, x)
    if left_idx == -1:
        return 0
    elif left_idx == right_idx:
        return 1
    return right_idx - left_idx + 1


def main():
    n = int(input())
    array = list(map(int, input().split()))
    q = int(input())
    items = list(map(int, input().split()))
    ans = [count_freq(array, x) for x in items]
    print(*ans)


if __name__ == "__main__":
    main()
