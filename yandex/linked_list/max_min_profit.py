def get_min_max_profit(arr):
    min_item = float("inf")
    max_item = float("-inf")
    min_gain = float("inf")
    max_gain = float("-inf")
    temp_min_idx, temp_max_idx, min_item_idx_2, max_item_idx_2 = 0, 0, 0, 0
    for i, elem in enumerate(arr):
        if min_item - elem < min_gain:
            i_1 = temp_min_idx
            j_1 = i
            min_gain = min_item - elem

        if elem < min_item:
            min_item = elem
            temp_min_idx = i

        if max_item - elem > max_gain:
            i_2 = temp_max_idx
            j_2 = i
            max_gain = max_item - elem

        if elem > max_item:
            max_item = elem
            temp_max_idx = i

    print(i_1 + 1, j_1 + 1)
    print(i_2 + 1, j_2 + 1)


def main():
    n = input()
    arr = list(map(int, input().split()))
    get_min_max_profit(arr)


if __name__ == "__main__":
    main()
