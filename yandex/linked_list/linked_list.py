from typing import Optional, List

"""
Не решена
Выполнение операций со списком
Ограничение времени
1 с
Ограничение памяти
256.0 Мб

Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt
Изначально у вас есть пустой список. Далее вам поступает q запросов. Каждый запрос одного из следующих типов:

Запрос 1-ого типа: добавить число y после x-ого числа в списке. Если x=0, то нужно сделать число  y новым началом списка
Запрос 2-ого типа: вывести число, которое находится на позиции x в списке
Запрос 3-его типа: удалить число, которое находится на позиции  x в списке

После каждого запроса второго типа необходимо вывести число, являющееся ответом. Гарантируется, что в списке в этот момент находилось хотя бы 
x элементов.

Также гарантируется, что если вам поступил запрос первого или третьего типа, то список к этому моменту содержал хотя бы 
x элементов.

Формат ввода
Первая строка содержит единственное число 
q - количество запросов.Далее следует q строк. Каждая из этих строк может иметь один из следующих видов:

Для запроса первого типа - "1 x y" (без кавычек)
Для запросов второго типа - "2 x" (без кавычек)
Для запросов третьего типа - "3 x" (без кавычек)

Формат вывода
Вывод должен состоять из  count строк, где count - количество запросов второго типа.
Каждая строка должна содержать ответ на соответствующий запрос в формате  value (где value - число, 
которое находится на позиции x).
"""


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head = node

    def get_item(self, idx):
        temp_item: Node = self.head
        temp_idx = 0
        while temp_item and temp_idx < idx - 1:
            temp_item = temp_item.nxt
            temp_idx += 1
        if temp_item:
            return temp_item.value

    def remove_element(self, idx: int):
        if self.head is None:
            return
        if idx == 1:
            self.head = self.head.nxt
            return

        temp_node = self.head
        prev_node = None
        temp_idx = 0
        while temp_node and temp_idx < idx - 1:
            prev_node = temp_node
            temp_node = temp_node.nxt
            temp_idx += 1
        if temp_node:
            prev_node.nxt = temp_node.nxt
        else:
            prev_node.nxt = None
            self.tail = prev_node

    def add_element_pos(self, pos, value):
        node = Node(value)
        if pos == 0:
            self.add_head(value)
        else:
            temp_idx = 0
            temp_item = self.head
            prev_item = None
            while temp_item and temp_idx < pos - 1:
                prev_item = temp_item
                temp_item = temp_item.nxt
                temp_idx += 1
            if temp_item:
                next_old_item = temp_item.nxt
                temp_item.nxt = node
                node.nxt = next_old_item

    def print_items(self):
        temp_item = self.head
        while temp_item:
            print(temp_item.value)
            temp_item = temp_item.nxt


def main():
    q = int(input().strip())
    linked_list = LinkedList()
    for _ in range(q):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            linked_list.add_element_pos(inp[1], inp[2])
        elif inp[0] == 2:
            item = linked_list.get_item(inp[1])
            print(item)
        else:
            linked_list.remove_element(inp[1])
        # linked_list.print_items()
    # linked_list.print_items()


if __name__ == "__main__":
    main()
