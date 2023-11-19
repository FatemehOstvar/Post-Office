import math
    # we are implementing heap, for that
    # we initialize a list that has our desired
    # size. to have a heap, one must
    # insert new elements and acknowledge it,
    # by adding to the heap size.
    # our list may have elements in it that are 
    # not part of the heap, meaning they have been popped
class MaxHeap:

    def __init__(self,list_size) -> None:
        self.values = [0] * list_size
        self.heap_size = 0

    
    def insert(self,element):
        self.heap_size +=1
        self.values[self.heap_size -1] = element
        self.bubble_up()


    def bubble_up(self):
        element_index = self.heap_size - 1
        while element_index>0:
            parent_index = self.find_parent_index(element_index)
            if parent_index < 0:
                break
            if self.values[parent_index] > self.values[element_index]:
                break
            element_index = self.swap(parent_index,element_index)


    def extract_max(self):
        self.values[0] = self.values[self.heap_size - 1]
        self.pop_it()
        self.bubble_down()


    def bubble_down(self):
        element_index = 0
        while element_index < self.heap_size:
            left_child_index = 2 * element_index + 1
            right_child_index = 2 * element_index + 2
            if left_child_index >= self.heap_size:
                break
            max_child_index = self.find_max_child_index(left_child_index, right_child_index)
            if self.values[max_child_index] <= self.values[element_index]:
                break
            element_index = self.swap(max_child_index, element_index)



    def swap(self, index1, index2):
        self.values[index1], self.values[index2] = self.values[index2], self.values[index1]
        return index1

    
    def find_parent_index(self, element_index):
        return math.floor((element_index - 1) / 2) if element_index > 0 else -1
        

    def find_max_child_index(self, left_child_index, right_child_index):
        if right_child_index < self.heap_size and self.values[right_child_index] > self.values[left_child_index]:
            return right_child_index
        else:
            return left_child_index


    def pop_it(self):
        popped = self.values[self.heap_size]
        self.heap_size -= 1
        return popped
        

    def push_it(self,element):
        self.heap_size += 1
        self.values[self.heap_size] = element


