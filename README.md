# Sorting Algorithm Runtime Comparison

## Task

Our task for this assignment was to:

> "Plot the runtimes for sorting input arrays of different sizes, at least for a quadratic sort and a linearithmic sort. Are the runtime plots shaped as we would expect from their analyses?"

As a result, we chose **Bubble Sort**, **Merge Sort**, and **Bucket Sort** as our sorting algorithms for this assignment.

## Time Complexities

The complexities for the algorithms are as follows:

- **Bubble Sort**: Quadratic \(O(n^2)\)
- **Merge Sort**: Linearithmic \(O(n \log n)\)
- **Bucket Sort**: Linear \(O(n + k)\), which simplifies to \(O(n)\) under certain conditions

After researching these sorting algorithms, we were able to implement them (as seen in the `assignment1.py` file, coded by Karan).

## Sorting Process

### What were we exactly sorting?

Before sorting, we needed to determine the sizes of the arrays. We worked with arrays of sizes: `100, 200, 400, 800, 1600, 3200, and 5000`, which we put into a NumPy array named **`sizes`**.

We used `for` loops to iterate through these values, creating arrays of each specified size. We then populated these arrays with random values between `0` and `10,000` and applied the sorting algorithms to them.

### Plotting the Results

We used the **Matplotlib** library to create a graph that plotted the runtimes against the array sizes. The graph was displayed in a GUI as output.

The output was as follows: ![image](https://github.com/user-attachments/assets/44d13671-0411-4e3f-8637-c2887712cfaa) 

### Observations

From our observations, the runtime plots aligned with our expectations based on the algorithm analyses:

- **Bubble Sort** shows quadratic growth in the graph.
- **Merge Sort** shows linearithmic growth.
- **Bucket Sort** exhibits linear growth in this case. Normally, Bucket Sort has a time complexity of \(O(n + k)\), where \(n\) is the number of elements and \(k\) is the number of buckets. In this instance, it appears that \(k\) is very small or effectively zero, which could explain the observed linear behavior on the graph. Understanding why \(k\) behaves this way was something we weren't able to figure out. That's something that may need some research. 





  
