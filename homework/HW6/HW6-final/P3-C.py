import matplotlib.pyplot as plt
from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue
from P3 import mergesortedlists, timeit, generatelists
 
# x = mergesortedlists(data, pqclass = NaivePriorityQueue)
naive_priority = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = NaivePriorityQueue, n_average = 5) 
heap_priority = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = HeapPriorityQueue, n_average = 5) 
python_priority = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = PythonHeapPriorityQueue, n_average = 5)

x_axis = [10, 20, 50, 100, 200, 500]

fig, ax = plt.subplots(1, 1, figsize=(10, 6), constrained_layout = True)
ax.set_xlabel(r'Number of Lists Merged', fontsize = 16)
ax.set_ylabel(r'Elapsed time in seconds', fontsize = 16)
ax.set_title(r'Comparing performance for different priority queues', fontsize = 16)

ax.plot(x_axis, naive_priority, label = r'Naive Priority Queue')
ax.plot(x_axis, heap_priority, label = r'Heap Priority Queue')
ax.plot(x_axis, python_priority, label = r'Python Heap Priority')
ax.legend(fontsize = 16)

plt.savefig('P3-C.png')

print(naive_priority)
print(heap_priority)
print(python_priority)

