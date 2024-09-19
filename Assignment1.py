import numpy as np
import time
import matplotlib.pyplot as plt

# Bubble Sort (Quadratic O(n^2))
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Track whether a swap was made
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swap was made, the array is already sorted
        if not swapped:
            break

# Merge Sort (O(n log n))
#generated this algorithm in chatgpt: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sorting the halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merging the sorted halves
        i = j = k = 0
        
        # Copy data to temporary arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Checking if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#bucket sort: O(N)
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Determine the number of buckets
    bucket_count = len(arr)
    
    # Create empty buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Find maximum and minimum values to scale the input
    min_value, max_value = min(arr), max(arr)
    
    # Place array elements into corresponding buckets
    for num in arr:
        index = int(bucket_count * (num - min_value) / (max_value - min_value + 1))
        buckets[index].append(num)
    
    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()  # Using Python's built-in Timsort, which is O(n log n)
    
    # Concatenate all buckets into the original array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array
 
#using the matplotlib library, we will plot the runtimes of the algorithms and show the 
#difference between time complexities.            
def plotOnGraph(sizes, bubble, merge, bucket): 
    # Plotting the results
    plt.figure(figsize=(10,6))
    plt.plot(sizes, bubble, label='Bubble Sort (O(n^2))', marker='o')
    plt.plot(sizes, merge, label='Merge Sort (O(n log n))', marker='o')
    plt.plot(sizes, bucket, label='Heap Sort (O(n log n))', marker='o')
    plt.title('Sorting Algorithms Time Complexity')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__": 
    # We will be using arrays of different sizes as below and to test out sorting speed. 
    sizes = np.array([100, 200, 400, 800, 1600, 3200, 5000])

    # These will be used to store the time used by sorting of each iteration of the array size per algorithm
    bubble_times = []
    merge_times = []
    bucket_times = []

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
    
    for size in sizes: 
        arr = np.random.randint(0,10000, size)
        start_time = time.time()
        bucket_sort(arr.copy())
        bucket_times.append(time.time() - start_time)
        
        
    plotOnGraph(sizes, bubble_times, merge_times, bucket_times)


