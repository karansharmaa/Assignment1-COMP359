# Sorting Algorithm Runtime Comparison

## Task

Our task for this assignment was to:

> "Plot the runtimes for sorting input arrays of different sizes, at least for a quadratic sort and a linearithmic sort. Are the runtime plots shaped as we would expect from their analyses?"

As a result, we chose **Bubble Sort**, **Merge Sort**, **Selection Sort**, and **Counting Sort** as our sorting algorithms for this assignment.

Our general assumption is that, regardless of the sorting method, the time required to sort an array increases with the array size.

## Time Complexities

The complexities for the algorithms are as follows:

- **Bubble Sort**: Quadratic \(O(n^2)\)
- **Merge Sort**: Linearithmic \(O(n \log n)\)
- **Counting Sort**: Linear \(O(n + k)\), which simplifies to \(O(n)\) under certain conditions
- **Selection Sort**: Quadratic \(O(n^2)\)

After researching these sorting algorithms, we were able to implement them (as seen in the `assignment1.py` file, coded by Karan and Amarnoor).

## Sorting Process

### What were we exactly sorting?

Before sorting, we needed to determine the sizes of the arrays. We worked with arrays of sizes: `100, 200, 400, 800, 1600, 3200, 5000, and 10000`, which we put into a NumPy array named **`sizes`**.

We used `for` loops to iterate through these values, creating arrays of each specified size. We then populated these arrays with random values between `0` and `10,000` and applied the sorting algorithms to them.

## Plotting the Results

We used the **Matplotlib** library to create a graph that plotted the runtimes against the array sizes. The graph was displayed in a GUI as output.

**The output was as follows (with BubbleSort)**: ![image](https://github.com/user-attachments/assets/1796cfcb-0102-42a0-8c74-d865c3e886da)
In this output, we can see that MergeSort and CountingSort are not portrayed fairly - mostly due to the runtime of BubbleSort being too high (clue: bubble sort is very inefficient). 

**Here is the output with BubbleSort taken out to represent MergeSort and CountingSort properly**: ![image](https://github.com/user-attachments/assets/39361c95-e1f9-4cd6-ad35-7b2ff2ca82cd)



## Observations

From our observations, the runtime plots aligned with our expectations based on the algorithm analyses:

- **Bubble Sort** shows quadratic growth in the graph. **Not an efficient sorting method**.
- **Merge Sort** shows linearithmic growth. **Very efficient**. 
- **Counting Sort** shows linear growth. **Most efficient**


## References

We used some help from chatgpt and did our research mostly on geeksforgeeks.org. 

- **ChatGPT Reference**: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
- **BubbleSort**: https://www.geeksforgeeks.org/bubble-sort-algorithm/
- **MergeSort**:  https://www.geeksforgeeks.org/merge-sort/
- **CountingSort**: https://www.geeksforgeeks.org/counting-sort/
- **MatPlotLib**: https://www.geeksforgeeks.org/matplotlib-tutorial/ & https://www.youtube.com/watch?v=D4VlmL3G4_o

  
