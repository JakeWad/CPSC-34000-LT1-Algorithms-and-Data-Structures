import time
import matplotlib.pyplot as plt
import random
# Heap Sort Algorithm
def heap_sort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# O(n^2) dummy function 
def insertion_sort(arr): 
    n = len(arr) 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, n): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
# O(nlogn) dummy function 
def merge_sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7] 
heap_sort(arr) 
print ("Sorted array is") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 
# Generating random array of size n
arr = [random.randint(1,1000) for i in range(1000)]
# Insertion Sort
start_time = time.time()
insertion_sort(arr)
end_time = time.time()
insertion_sort_time = end_time - start_time
# Heap Sort
start_time = time.time()
heap_sort(arr)
end_time = time.time()
heap_sort_time = end_time - start_time
# Merge Sort
start_time = time.time()
merge_sort(arr)
end_time = time.time()
merge_sort_time = end_time - start_time
# Built-in Sort
start_time = time.time()
sorted(arr)
end_time = time.time()
builtin_sort_time = end_time - start_time
# Plotting the graph
x = ["Insertion Sort", "Heap Sort", "Merge Sort", "Built-in Sort"]
y = [insertion_sort_time, heap_sort_time, merge_sort_time, builtin_sort_time]
plt.plot(x, y)
plt.xlabel("Sorting Algorithm")
plt.ylabel("Time (sec)")
plt.title("Comparison of Algorithms")
plt.show()
