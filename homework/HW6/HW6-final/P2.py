from math import floor
from typing import List

class Heap:
    
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in a heap
        self.build_heap()
    
    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1
    
    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)
    
    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
            if self.size == 0:
                return '\\--'
            elif idx < self.size:
                buf = prefix
                if left:
                    buf = buf + "|-- "
                else:
                    buf = buf + "\\-- "
                # buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
                buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

                new_prefix = prefix
                if left:
                    new_prefix = new_prefix + "|   "
                else:
                    new_prefix = new_prefix + "    "

                return buf + \
                        self.to_string(new_prefix, self.left(idx), True) + \
                        self.to_string(new_prefix, self.right(idx), False)
            else:
                return ''

    def __str__(self) -> str:
        return self.to_string()
    
    def __len__(self) -> int:
        return self.size

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError
    
    def heapify(self, idx: int) -> None: # Close but not entirely returning the minimum
        
        smallest = idx
        if self.left(idx) < self.size and self.elements[self.left(idx)] < self.elements[idx]:
            smallest = self.left(idx)
        
        if self.right(idx) < self.size and self.elements[self.right(idx)] < self.elements[idx]:
            smallest = self.right(idx)

        if smallest != idx:
            self.elements[idx], self.elements[smallest] = self.elements[smallest], self.elements[idx]

            self.heapify(smallest)

    def build_heap(self) -> None:

        for i in range(self.size):
            self.heapify(i)

    # Iterate through the heap to compare your insert to heap value
    # Compare what you've added to the parent of what you've added and swap accordingly
    def heappush(self, key: int) -> None: # How to account for if the input key is less than lowest value
        self.elements.append(key)
        self.size += 1
        self.build_heap()

    def heappop(self) -> int: # return self.parent?
        h = self.elements.pop()
        self.heapify(h)

class MinHeap(Heap):

    def __init__(self):
        super(Heap, self).__init__()

    def compare(self, a, b:
        pass # TODO

class MaxHeap(Heap):

    def __init__(self):
        super(Heap, self).__init__()


    def compare(self, a, b):
        pass # TODO
        
        # Implement the code below
        # largest = idx
        # if self.left(idx) < self.size and self.elements[self.left(idx)] > self.elements[idx]:
        #     largest = self.left(idx)
        
        # if self.right(idx) < self.size and self.elements[self.right(idx)] > self.elements[idx]:
        #     largest = self.right(idx)

        # if largest != idx:
        #     self.elements[idx], self.elements[largest] = self.elements[largest], self.elements[idx]

        #     self.heapify(largest)