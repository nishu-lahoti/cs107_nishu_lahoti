from random import sample
from time import time
from P2 import MinHeap
import heapq

class PriorityQueue:

    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
    
    def __len__(self):
        return len(self.elements)
    
    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

def mergesortedlists(lists, pqclass = PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))
    
    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))
        
    return merged

def generatelists(n, length = 20, dictionary_path='./words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists

def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = PriorityQueue, n_average = 5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    
    return elapsed


class NaivePriorityQueue(PriorityQueue):

    # Super initializing NaivePriorityQueue
    def __init__(self, max_size):
        super().__init__(max_size)

    def put(self, val):
        
        # IndexError if the elements list is greater than the max size
        if len(self.elements) > self.max_size - 1:
            raise IndexError("Max size already reached")

        # Append element
        self.elements.append(val)

    def get(self):

        # Use peek's minimum finding ability to find and set min val
        getVal = self.peek()

        # Remove min val
        self.elements.remove(min(self.elements))
        return getVal

    def peek(self):

        # IndexError if the elements list is greater than the max size
        if not self.elements:
            raise IndexError("Empty priority queue.")

        # Set and return minVal
        minVal = min(self.elements)
        return minVal

class HeapPriorityQueue(PriorityQueue):

    def __init__(self, max_size):

        # Different metholodogy for initialization based on conversations with Hayoun in OH.

        # super().__init__(max_size)
        # Set elements to empty MinHeap
        # Set max_size to max_size
        self.elements = MinHeap([])
        self.max_size = max_size

    
    def put(self, val):

        # IndexError if the elements list is greater than the max size
        if len(self.elements) > self.max_size - 1:
            raise IndexError("Max size already reached")
        
        # Utilize the heappush from MinHeap method
        self.elements.heappush(val)

    def get(self):

        if not self.elements:
            raise IndexError("Empty priority queue.")
        
        # Utilize the heappop from MinHeap method
        return self.elements.heappop()

    def peek(self):

        # IndexError if the elements list doesn't exist
        if not self.elements:
            raise IndexError("Empty priority queue.")
        
        # Guidance from Hayoun - the first element of elements
        return self.elements.elements[0]

class PythonHeapPriorityQueue(PriorityQueue):

    def __init__(self, max_size):

        # Different metholodogy for initialization based on conversations with Hayoun in OH.

        # super().__init__(max_size)
        self.elements = []
        self.max_size = max_size
    
    def put(self, val):
        
        # IndexError if the elements list doesn't exist
        if len(self.elements) > self.max_size -1:
            raise IndexError("Max size already reached")
        
        # Python's heappush methodology
        heapq.heappush(self.elements, val)

    def get(self):
        
        # IndexError if the elements list doesn't exist
        if not self.elements:
            raise IndexError("Empty priority queue.")
        
        # Python's heappop methodology
        return heapq.heappop(self.elements)

    def peek(self):
        
        # IndexError if the elements list doesn't exist
        if not self.elements:
            raise IndexError("Empty priority queue.")
        
        # Return the very first element of the list
        return self.elements[0]
