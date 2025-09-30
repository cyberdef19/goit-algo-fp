
class Node:

    def __init__(self, val: any):
        self.next:Node = None
        self.value = val

class LinkedList:

    def __init__(self):
        self.tail: Node = None
        self.head: Node = None

    def print(self):

        temp = self.head
        values = []
        while temp:
            values.append(temp.value)
            temp = temp.next
        print(values)

    def reverse_1(self):

        values = []
        temp = self.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        values.reverse()
        temp = self.head
        i = 0
        while temp:
            temp.value = values[i]
            i += 1
            temp = temp.next

    def reverse_2(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        nodes.reverse()
        new_head: Node = None
        new_tail: Node = None
        for i, n in enumerate(nodes):
            if i == 0:
                new_head = nodes[0]
                new_head.next = nodes[1]
            elif i == len(nodes) - 1:
                new_tail = nodes[i]
                new_tail.next = None
            else:
                nodes[i].next = nodes[i + 1]
        return new_head

    def __add__(self, other: "LinkedList") -> "LinkedList":

        if not isinstance(other, LinkedList):
            return self

        if other.head is None:
            return self
        if self.head is None:
            return other

        self.tail.next = other.head
        self.tail = other.tail
        self.insertion_sort()
        return self

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self.insert_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head


    def insert_sorted(self, head: Node, node: Node) -> Node:
        if head is None or node.value < head.value:
            node.next = head
            return node

        current = head
        while current.next and current.next.value < node.value:
            current = current.next

        node.next = current.next
        current.next = node
        return head

    def insert_tail(self, node: Node) -> Node:
        if self.tail is None and self.head is None:
            self.tail = node
            self.head = node
            return node

        self.tail.next = node
        self.tail = node
        return self.tail

    def insert_head(self, node: Node) -> Node:
        if self.tail is None and self.head is None:
            self.tail = node
            self.head = node
            return node
        node.next = self.head
        self.head = node
        return self.head

    def insert(self, node: Node, index:int) -> Node:

        if index == 0:
            return self.insert_head(node)

        if index == 1:
            return self.insert_tail(node)

        tempnode = self.head
        prev = None
        i = 0
        while tempnode and i < index :
            prev = tempnode
            tempnode = tempnode.next
            i += 1
        if i != index:
            raise IndexError("Індекс знаходиться за межами списку")

        prev.next = node
        node.next =tempnode

        if tempnode is None:
            self.tail = node

        return node

    def delete(self, value: any):
        if not self.head:
            return

        if self.head.value == value:
            if self.head.next is not None:
                self.head = self.head.next
            elif self.head.next is None and self.head == self.tail:
                self.head = None
                self.tail = None


        temp = self.head
        prev = None
        while temp.value != value and temp:
            prev = temp
            temp = temp.next
        if temp is None:
            raise ValueError("Вузла з таким значенням у списку немає")

        prev.next = temp.next

        if temp == self.tail:
            self.tail = prev


linkedList = LinkedList()
node1 = Node(10)
linkedList.insert(node1, 0)
node2 = Node(5)
linkedList.insert(node2, 1)
node3 = Node(0)
linkedList.insert(node3, 2)
node4 = Node(12)
linkedList.insert(node4, 3)
node5 = Node(15)
linkedList.insert(node5, 4)
node6 = Node(9)
linkedList.insert(node6, 4)
node7 = Node(20)
linkedList.insert(node7, 3)
node8 = Node(17)
linkedList.insert(node8, 3)
linkedList.print()
current = linkedList.reverse_2()

while current:
    print(current.value)
    current = current.next

linkedList.insertion_sort()
linkedList.print()














