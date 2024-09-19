import numpy as np
import time
import matplotlib.pyplot as plt

# Bubble Sort (Quadratic O(n^2))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort (O(n log n))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

 
#using the matplotlib library, we will plot the runtimes of the algorithms and show the 
#difference between time complexities.            
def plotOnGraph(sizes, bubble_times, merge_times): 
    # Plotting the results
    plt.figure(figsize=(10,6))
    plt.plot(sizes, bubble_times, label='Bubble Sort (O(n^2))', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort (O(n log n))', marker='o')
    plt.title('Sorting Algorithms Time Complexity')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main(): 
    # We will be using arrays of different sizes as below and to test out sorting speed. 
    sizes = np.array([100, 200, 400, 800, 1600, 3200, 5000])

    # These will be used to store the time used by sorting of each iteration of the array size per algorithm
    bubble_times = []
    merge_times = []

    # Measure time for Bubble Sort - these times will be stored in bubble_times 
    #and be plotted  into the graph we will use to show runtimes. 
    for size in sizes:
        #random integers between 0 and 10000 will be choosen and put in to whatever size array is being iterated
        #into the for loop. 
        arr = np.random.randint(0, 10000, size)
        #using time library, we will calculate how long it takes to sort using bubble sort. 
        start_time = time.time()
        bubble_sort(arr.copy())
        bubble_times.append(time.time() - start_time)

    # Measure time for Bubble Sort - these times will be stored in bubble_times 
    #and be plotted  into the graph we will use to show runtimes. 
    for size in sizes:
        #random integers between 0 and 10000 will be choosen and put in to whatever size array is being iterated
        #into the for loop. 
        arr = np.random.randint(0, 10000, size)
        #using time library, we will calculate how long it takes to sort using merge sort
        start_time = time.time()
        merge_sort(arr.copy())
        merge_times.append(time.time() - start_time)
        
    plotOnGraph(sizes, bubble_times, merge_times)



main()