import matplotlib.pyplot as plt

# Import methods from P3
# from P3 import * <-- Another option
from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue
from P3 import mergesortedlists, timeit, generatelists
 
# Set variables for each priority queue type based on timeit statement
naive_priority = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = NaivePriorityQueue, n_average = 5) 
heap_priority = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = HeapPriorityQueue, n_average = 5) 
python_priority = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass = PythonHeapPriorityQueue, n_average = 5)

# Set x-axis
x_axis = [10, 20, 50, 100, 200, 500]

# Set figure size and labels
fig, ax = plt.subplots(1, 1, figsize=(10, 6), constrained_layout = True)
ax.set_xlabel(r'Number of Lists Merged', fontsize = 16)
ax.set_ylabel(r'Elapsed time in seconds', fontsize = 16)
ax.set_title(r'Comparing performance for different priority queues', fontsize = 16)

# Plot each priority queue
ax.plot(x_axis, naive_priority, label = r'Naive Priority Queue')
ax.plot(x_axis, heap_priority, label = r'Heap Priority Queue')
ax.plot(x_axis, python_priority, label = r'Python Heap Priority')
ax.legend(fontsize = 16)

# Save the plot figure
plt.savefig('P3-C.png')