import numpy as np
import time
import matplotlib.pyplot as plt

# Bubble Sort (Quadratic O(n^2))
# created with help from chatgpt: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
# and with help from geeksforgeeks: https://www.geeksforgeeks.org/bubble-sort-algorithm/
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

# Merge Sort linearithmic (O(n log n))
# created with help from chatgpt: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
# and with help from geeksforgeeks: https://www.geeksforgeeks.org/merge-sort/
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
            
#Counting sort: linear O(n)
#created with help from geeksforgeeks and chatgpt
#geeksforgeek: https://www.geeksforgeeks.org/counting-sort/
#chatgpt: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Find the maximum and minimum element in the array
    max_val = max(arr)
    min_val = min(arr)
    
    # Initialize the count array
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    
    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Modify the count array by adding the previous counts (cumulative)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Output array to store the sorted elements
    output = [0] * len(arr)
    
    # Build the sorted array
    for num in range(len(arr) - 1, -1, -1):
        output[count[arr[num] - min_val] - 1] = arr[num]
        count[arr[num] - min_val] -= 1
    
    return output
# Selection Sort quadratic (O(n^2)
# Created with help from geeksforgeeks:  https://www.geeksforgeeks.org/selection-sort-algorithm-2/
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
 
#using the matplotlib library, we will plot the runtimes of the algorithms and show the 
#difference between time complexities.          
#learned how to do this from: https://www.geeksforgeeks.org/matplotlib-tutorial/  
def plotOnGraph(sizes, bubble, merge, counting, select): 
    # Plotting the results
    plt.figure(figsize=(10,6))
    #plt.plot(sizes, bubble, label='Bubble Sort (O(n^2))', marker='o')
    plt.plot(sizes, merge, label='Merge Sort (O(n log n))', marker='o')
    plt.plot(sizes, counting, label='Counting Sort (O(n))', marker='o')
    #plt.plot(sizes, select, label='Selection Sort (O(n^2))', marker='o')
    plt.title('Sorting Algorithms Time Complexity')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__": 
    
    # We will be using arrays of different sizes as below and to test out sorting speed. 
    sizes = np.array([100, 200, 400, 800, 1600, 3200, 5000, 10000])

    # These will be used to store the time used by sorting of each iteration of the array size per algorithm
    bubble_times = []
    merge_times = []
    counting_times = []
    select_times = []

    # Measure time for Bubble Sort - these times will be stored in bubble_times 
    #and be plotted  into the graph we will use to show runtimes. 
    for size in sizes:
        #random integers between 0 and 10000 will be choosen and put in to whatever size array is being iterated
        #into the for loop. 
        arr = np.random.randint(0, 10000, size)
        #using time library, we will calculate how long it takes to sort using bubble sort. 
        start_time = time.perf_counter()
        bubble_sort(arr.copy())
        bubble_times.append((time.perf_counter() - start_time) * 1000)

    # Measure time for Merge Sort - these times will be stored in merge_times 
    #and be plotted  into the graph we will use to show runtimes. 
    for size in sizes:
        #random integers between 0 and 10000 will be choosen and put in to whatever size array is being iterated
        #into the for loop. 
        arr = np.random.randint(0, 10000, size)
        #using time library, we will calculate how long it takes to sort using merge sort
        start_time = time.perf_counter()
        merge_sort(arr.copy())
        merge_times.append((time.perf_counter() - start_time) * 1000)
    
    # Measure time for Counting Sort - these times will be stored in counting_times 
    #and be plotted  into the graph we will use to show runtimes. 
    for size in sizes: 
        #random integers between 0 and 10000 will be choosen and put in to whatever size array is being iterated
        #into the for loop. 
        arr = np.random.randint(0,10000, size)
        #using time library, we will calculate how long it takes to sort using merge sort
        start_time = time.perf_counter()
        counting_sort(arr.copy())
        counting_times.append((time.perf_counter() - start_time) * 1000)

    # Measure time for Selection Sort - these times will be stored in select_times 
    #and be plotted  into the graph we will use to show runtimes
    for size in sizes: 
        #random integers between 0 and 10000 will be choosen and put in to whatever size array is being iterated
        #into the for loop. 
        arr = np.random.randint(0,10000, size)
        #using time library, we will calculate how long it takes to sort using selection sort
        start_time = time.perf_counter()
        selection_sort(arr.copy())
        select_times.append((time.perf_counter() - start_time) * 1000)
        
    #calling the graph plotting method to create a graph and display it in a GUI
    plotOnGraph(sizes, bubble_times, merge_times, counting_times, select_times)


