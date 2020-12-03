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

    # Implementing compare method per prompt
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError
    
    def heapify(self, idx: int) -> None: 
        
        # ACADEMIC HONESTY STATEMENT
        # I worked on this problem in office hours on 11/20, 11/23, and 11/24.
        # In hoping to understand this problem better, I consulted both my teammates and fellow classmates during these sessions.
        # For this particular problem, I reviewed my solution with Vikram Shasty and Timothy Williamson. We compared our outputs
        # and each adapted our code based on the consensus we arrived at for the best methodology.

        # Functions as a min heap method    
        smallest = idx
        heap_length = self.size - 1

        # Compare values and indexes of left against elements list
        if self.left(idx) <= heap_length and self.compare(self.elements[self.left(idx)], self.elements[idx]):
            smallest = self.left(idx)

        # Compare values and indexes of right against elements list
        if self.right(idx) <= heap_length and self.compare(self.elements[self.right(idx)], self.elements[smallest]):
            smallest = self.right(idx)

        # Swapping for lowest values
        if smallest != idx:
            self.swap(idx, smallest)
            self.heapify(smallest)

    def build_heap(self) -> None:

        # Building the heap based on the last element of heap and iterating until floor
        for i in reversed(range(len(self.elements) // 2)):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        self.elements.append(key)

        # Increase size of element list and set value for element before last
        self.size += 1        
        current = self.size - 1

        # Compare current against parent value to percolate down tree
        while self.compare(self.elements[current], self.elements[self.parent(current)]) \
            and self.parent(current) >= 0:
            
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def heappop(self) -> int:

        # Error if heap is empty
        if self.size == 0:
            raise IndexError("No heap to pop.")
        
        # Swapping first and last elements
        self.swap(0, self.size - 1)

        # Set value for final element
        root = self.elements.pop(self.size - 1)
        
        # Reduce size, restore heap, return lowest value
        self.size -=1
        self.heapify(0)
        return root


class MinHeap(Heap):

    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
    
    # Comparison for lowest value.
    # Could not figure out how to compare if VIOLATES True
    def compare(self, a: int, b: int) -> bool:
        return a < b


class MaxHeap(Heap):

    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
    
    # Comparison for highest value.
    # Could not figure out how to compare if VIOLATES True
    def compare(self, a: int, b: int) -> bool:
        return a > b