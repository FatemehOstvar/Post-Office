class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.first
            self.first = new_node
            self.first.next = temp

        self.size += 1

    def pop(self):
        if not self.first:
            return None

        temp = self.first

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.size -= 1

        return temp.value


    def get_last_element(self):
        if self.last:
            return self.last.value
        return None


    def display(self):
        current = self.first
        print("Stack:")
        while current:
            print(current.value)
            current = current.next

    def peek(self):
        if self.first is not None:
            return self.first.value
        return None

    def get_stack(self):
        stack = []
        current = self.first
        while current:
            stack.append(current.value)
            current = current.next
        return stack