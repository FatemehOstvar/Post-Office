from tkinter import *
from Stack import *
class Node:
    def __init__(self, name, sender, recipient, distance, tracking_code):
        self.next = None
        self.name = name
        self.sender = sender
        self.recipient = recipient
        self.distance = distance
        self.tracking_code = tracking_code
        self.status_stack = Stack()


class Parcel:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, name, sender, recipient, distance, tracking_code):
        new_node = Node(name, sender, recipient, distance, tracking_code)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if not self.first:
            return None

        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.size -= 1
        return temp.value

    def get(self):
        values = []
        current = self.first
        while current:
            values.append(f"name: {current.name} _"
                          f"sender: {current.sender} _"
                          f"recipient: {current.recipient} _"
                          f"distance: {current.distance} _"
                          f"tracking code: {current.tracking_code} _"
                          f"status: {current.status_stack.peek()} _")
            current = current.next
        return values

    def find(self, key):
        if not self.first:
            return None
        start = 0
        end = self.size - 1

        while start <= end:

            mid = self.get_mid(start, end)
            mid_node = self.get_by_index(mid)

            if int(mid_node.tracking_code) == int(key):
                return mid_node.status_stack.get_stack()
            elif int(key) < int(mid_node.tracking_code):
                end = mid - 1
            else:
                start = mid + 1


    def find_shortest(self):
        current = self.first

        while current:
            if int(current.distance) < current.next.distance:
                return current.status_stack.get_stack( )

            current = current.next

        return None
    def set(self, key, tobe):
        current = self.first
        while current:
            if int(current.tracking_code) == int(key):
                if "delivered" in current.status_stack.get_stack():
                    print("it is delivered and cannot be changed anymore")
                    break
                # if current.status_stack.is_empty():
                #     break
                current.status_stack.push(tobe)
                print("Done:)")
                # current.value["status"].get_stack().status_stack.push(tobe)
            current = current.next


    def get_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.first
        for i in range(index):
            current = current.next
        return current

    def get_mid(self, start, end):
        return (start + end) // 2


    # Binary search
    def find_and_access_stack(self, key):
        if not self.first:
            return None
        start = 0
        end = self.size - 1

        while start <= end:

            mid = self.get_mid(start, end)
            mid_node = self.get_by_index(mid)

            if int(mid_node.tracking_code) == int(key):
                return mid_node.status_stack
            elif int(key)< int(mid_node.tracking_code):
                end = mid - 1
            else:
                start = mid + 1

    def find_node(self, key):
        if not self.first:
            return None
        start = 0
        end = self.size - 1

        while start <= end:

            mid = self.get_mid(start, end)
            mid_node = self.get_by_index(mid)

            if int(mid_node.tracking_code) == int(key):
                return mid_node
            elif int(key) < int(mid_node.tracking_code):
                end = mid - 1
            else:
                start = mid + 1

    def display_queue(self):
        queue_window = Toplevel( )
        queue_window.iconify( )
        queue_display = Text(queue_window)
        queue_window.deiconify( )
        queue_display.insert(END, str(self.get()))
        queue_display.pack( )

    def display_specific_queue(self,tracking_code):
        results = self.find(tracking_code)
        queue_window = Toplevel( )
        queue_window.iconify( )
        queue_display = Text(queue_window)

        if results:
            queue_display.insert(END, self.find(tracking_code))
        else:
            queue_display.insert(END, "No Parcel Was Found With This Tracking Code")
        queue_window.deiconify( )
        queue_display.pack( )



#
# t= Queue()
# t.enqueue("2")
# t.enqueue("me")
# t.first.status_stack.push(2)
# t.first.status_stack.push("d")
# var = t.first.status_stack.peek()
# tt = t.first.status_stack.get_stack()
