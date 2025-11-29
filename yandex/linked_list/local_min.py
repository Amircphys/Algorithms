def delete_local_max(arr):
    new_arr = [arr[0]]
    for i in range(1, len(arr) - 1):
        if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
            continue
        new_arr.append(arr[i])
    if len(arr) > 1:
        new_arr.append(arr[-1])
    return new_arr


def main():
    n = input()
    arr = list(map(int, input().split()))
    new_arr = delete_local_max(arr)
    print(len(new_arr))
    print(*new_arr)


if __name__ == "__main__":
    main()
