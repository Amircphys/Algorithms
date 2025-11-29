def bin_search(array, x):
    left_idx, right_idx = 0, len(array) - 1
    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        middle_item = array[middle_idx]
        if middle_item == x:
            return middle_idx
        elif middle_item < x:
            left_idx = middle_idx + 1
        else:
            right_idx = middle_idx - 1
    return -1


def main():
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())
    ans = bin_search(array, x)
    print(ans)


if __name__ == "__main__":
    main()
