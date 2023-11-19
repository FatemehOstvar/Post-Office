class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current_head

    def unshift(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current

    def set(self, index, val):
        found_node = self.get(index)
        if found_node:
            found_node.val = val
            return True
        return False

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return bool(self.push(val))
        if index == 0:
            return bool(self.unshift(val))

        new_node = Node(val)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return True


# Instantiate the SinglyLinkedList and perform operations
sll = SinglyLinkedList()
sll.push(100)
sll.push(201)
sll.push(250)
sll.push(350)
sll.insert(2,33)
sll.set(4,55)

for i in range(sll.length):
    print(sll.get(i).val)
