class PriorityQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.values = [None] * max_size

    def enqueue(self, val, priority):
        if self.current_size < self.max_size:
            self.values[self.current_size] = Node(val, priority)
            self.bubbleUp(self.current_size)
            self.current_size += 1
        else:
            print("Queue is full")

    def bubbleUp(self, index):
        element = self.values[index]
        while index > 0:
            parent_index = (index - 1) // 2
            parent = self.values[parent_index]
            if element.priority >= parent.priority:
                break
            self.values[parent_index] = element
            self.values[index] = parent
            index = parent_index

    def dequeue(self):
        if self.current_size > 0:
            min_val = self.values[0]
            self.current_size -= 1
            self.values[0] = self.values[self.current_size]
            self.sinkDown(0)
            return min_val
        else:
            print("Queue is empty")

    def sinkDown(self, index):
        element = self.values[index]
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            swap = None

            if left_child_index < self.current_size:
                left_child = self.values[left_child_index]
                if left_child.priority < element.priority:
                    swap = left_child_index
            if right_child_index < self.current_size:
                right_child = self.values[right_child_index]
                if (swap is None and right_child.priority < element.priority) or (swap is not None and right_child.priority < left_child.priority):
                    swap = right_child_index

            if swap is None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = element
            index = swap

    def get_lowest_priority(self):
        if self.current_size > 0:
            return self.values[0]
        else:
            return None


class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
#
# ER = PriorityQueue(5)
# ER.enqueue("common cold", 5)
# ER.enqueue("gunshot wound", 1)
# ER.enqueue("high fever", 4)
# ER.enqueue("broken arm", 2)
# ER.enqueue("glass in foot", 3)
#
# print(ER.get_lowest_priority().val)
