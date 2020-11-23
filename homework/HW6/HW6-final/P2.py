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
    
    def heapify(self, idx: int) -> None: 
        if self.compare(self.elements[idx], self.elements[self.parent(idx)]):
            self.swap(idx, self.parent(idx))

    def verify_heap(self):
        
        heap = False
        for i in range(self.size - 1, 0, -1):
            if self.compare(self.elements[i], self.elements[self.parent(i)]):
            # if self.elements[i] < self.elements[self.parent(i)]:
                heap = True
            return heap

    def build_heap(self) -> None:

        while self.verify_heap():
            for i in range(self.size - 1, 0, -1):
                self.heapify(i)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1
        self.build_heap()

    def heappop(self) -> int:

        if self.size == 0:
            raise IndexError("No heap to pop.")
        
        self.swap(0, self.size - 1)
        root = self.elements.pop(self.size - 1)
        
        self.size -=1
        self.build_heap()
        return root


class MinHeap(Heap):

    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
    
    def compare(self, a: int, b: int) -> bool:
        smallest = False
        
        if a < b:
            smallest = True
        return smallest


class MaxHeap(Heap):

    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
    
    def compare(self, a: int, b: int) -> bool:
        largest = False
        
        if a > b:
            largest = True
        return largest