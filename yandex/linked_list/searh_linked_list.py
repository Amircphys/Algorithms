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
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    ll = LinkedList(arr)
    for _ in range(q):
        idx = ll.search_element(int(input()))
        print(idx)


if __name__ == "__main__":
    main()
