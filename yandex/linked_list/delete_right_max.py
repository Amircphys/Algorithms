class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.max = None

    def add_element(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.max = node
            return
        self.tail.next = node
        if self.max <= value:
            self.max = node

    def delete_right_max(self):
        pass


def delete_right_max(arr):
    max_val = max(arr)
    right_idx = len(arr) - 1
    while right_idx > 0:
        if arr[right_idx] == max_val:
            _ = arr.pop(right_idx)
            return arr
        right_idx -= 1
    return arr


def main():
    n = input()
    arr = list(map(int, input().split()))
    result = delete_right_max(arr)
    print(*result)


if __name__ == "__main__":
    main()
