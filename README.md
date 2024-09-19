# Sorting Algorithm Runtime Comparison

## Task

Our task for this assignment was to:

> "Plot the runtimes for sorting input arrays of different sizes, at least for a quadratic sort and a linearithmic sort. Are the runtime plots shaped as we would expect from their analyses?"

As a result, we chose **Bubble Sort**, **Merge Sort**, and **Counting Sort** as our sorting algorithms for this assignment.

## Time Complexities

The complexities for the algorithms are as follows:

- **Bubble Sort**: Quadratic \(O(n^2)\)
- **Merge Sort**: Linearithmic \(O(n \log n)\)
- **Counting Sort**: Linear \(O(n + k)\), which simplifies to \(O(n)\) under certain conditions

After researching these sorting algorithms, we were able to implement them (as seen in the `assignment1.py` file, coded by Karan).

## Sorting Process

### What were we exactly sorting?

Before sorting, we needed to determine the sizes of the arrays. We worked with arrays of sizes: `100, 200, 400, 800, 1600, 3200, and 5000`, which we put into a NumPy array named **`sizes`**.

We used `for` loops to iterate through these values, creating arrays of each specified size. We then populated these arrays with random values between `0` and `10,000` and applied the sorting algorithms to them.

## Plotting the Results

We used the **Matplotlib** library to create a graph that plotted the runtimes against the array sizes. The graph was displayed in a GUI as output.

**The output was as follows**: ![image](https://github.com/user-attachments/assets/44d13671-0411-4e3f-8637-c2887712cfaa) 

## Observations

From our observations, the runtime plots aligned with our expectations based on the algorithm analyses:

- **Bubble Sort** shows quadratic growth in the graph.
- **Merge Sort** shows linearithmic growth.
- **Counting Sort** shows linear growth. Usually, counting sort has a time complexity of \(O(n + k)\), where \(n\) is the number of elements and \(k\) is the range of input values.
In this case, we noticed an unusual result where the \(k\) value appeared to be zero. Due to this, we encountered difficulties determining the exact reason for this outcome. This is something that may need some research. 



## References

We used some help from chatgpt and did our research mostly on geeksforgeeks.org. 

- **ChatGPT Reference**: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
- **BubbleSort**: https://www.geeksforgeeks.org/bubble-sort-algorithm/
- **MergeSort**:  https://www.geeksforgeeks.org/merge-sort/
- **CountingSort**: https://www.geeksforgeeks.org/counting-sort/
- **MatPlotLib**: https://www.geeksforgeeks.org/matplotlib-tutorial/ & https://www.youtube.com/watch?v=D4VlmL3G4_o

  
