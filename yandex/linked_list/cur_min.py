def get_cur_min(arr):
    mins = [item for item in arr]
    cur_min = float("inf")
    for i in range(len(arr)):
        cur_min = min(cur_min, arr[i])
        mins[i] = cur_min
    return mins


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, items):
        self.head = None
        self.tail = None
        self.add_elements(items)

    def add_elements(self, elements):
        for element in elements:
            self.add_one_element(element)

    def add_one_element(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get_cur_min(self):
        temp_min = float("inf")
        temp_node = self.head
        while temp_node:
            print(min(temp_min, temp_node.value), end=" ")
            temp_node = temp_node.next

    def search_element(self, element):
        temp_node = self.head
        idx = 1
        while temp_node:
            if temp_node.value == element:
                return idx
            idx += 1
            temp_node = temp_node.next
        return -1


def main():
    n = input()
    arr = list(map(int, input().split()))
    # result = get_cur_min(arr)
    # print(*result)
    ll = LinkedList(arr)
    ll.get_cur_min()


if __name__ == "__main__":
    main()
