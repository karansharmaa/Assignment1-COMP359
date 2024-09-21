# Sorting Algorithm Runtime Comparison

## Task

Our task for this assignment was to:

> "Plot the runtimes for sorting input arrays of different sizes, at least for a quadratic sort and a linearithmic sort. Are the runtime plots shaped as we would expect from their analyses?"

As a result, we chose **Bubble Sort**, **Merge Sort**, **Selection Sort**,**Counting Sort**, and **Quick Sort** as our sorting algorithms for this assignment.

Our general assumption is that, regardless of the sorting method, the time required to sort an array increases with the array size.

## Division Of Work
- **Karan**: created and implemented the matplotlib plot GUI, implemented bubble sort, merge sort and counting sort. Created the readme.md.
- **Amarnoor**: implemented selection sort. Created the formal report documentation. Contributed to the readme.md.
- **Vibhu**: Created the Tkinter GUI which allows user to compare two algorithms. Also implemented QuickSort.
  
## Time Complexities

The complexities for the algorithms are as follows:

- **Bubble Sort**: Quadratic \(O(n^2)\)
- **Merge Sort**: Linearithmic \(O(n \log n)\)
- **Counting Sort**: Linear \(O(n + k)\), which simplifies to \(O(n)\) under certain conditions
- **Selection Sort**: Quadratic \(O(n^2)\)
- **QuickSort** Linear \(O(n)\). 

After researching these sorting algorithms, we were able to implement them (as seen in the `assignment1.py` file, coded by Karan, Vibhu and Amarnoor).

## Sorting Process

### What were we exactly sorting?

Before sorting, we needed to determine the sizes of the arrays. We worked with arrays of sizes: `100, 200, 400, 800, 1600, 3200, 5000, and 10000`, which we put into a NumPy array named **`sizes`**.

We used `for` loops to iterate through these values, creating arrays of each specified size. We then populated these arrays with random values between `0` and `10,000` and applied the sorting algorithms to them.

## Output / Plotting the Results

Our output procedure was as follows: 
- User runs the code
- The tkinter (tk) GUI gets displayed asking user to choose between two algorithms.
  
  ![WhatsApp Image 2024-09-20 at 9 10 18 PM](https://github.com/user-attachments/assets/5588cece-acbb-4836-b173-d7014bbe1d14)
  
- User chooses the two algorithms they'd like to compare
- With help from the **Matplotlib** library, the program creates a plot graph in a separate GUI showcasing the results and comparing the runtimes of the two algorithms chosed. 
  ![image](https://github.com/user-attachments/assets/8d63b972-555d-4010-a341-bf4ce86eff40)
  ![WhatsApp Image 2024-09-20 at 9 10 53 PM](https://github.com/user-attachments/assets/60d0dfc8-54ef-4568-a0fd-8d52083a3734)
  ![WhatsApp Image 2024-09-20 at 9 11 19 PM](https://github.com/user-attachments/assets/19e53fcd-8846-4874-9d74-749004239b9a)

- **Below is the result of all algorithms being compared at once:** ![image](https://github.com/user-attachments/assets/793bed4a-cb58-471e-a3c5-2a6a05733301)

## Code
This project requires the installation of the `NumPy`, `Matplotlib` and `Tkinter (Tk)` libraries in Python to function correctly.

To install the necessary libraries, run the following commands in your terminal or command prompt:

```bash
pip3 install matplotlib
pip3 install numpy
pip3 install tk
```
  

## Observations

From our observations, the runtime plots aligned with our expectations based on the algorithm analyses:

- **Bubble Sort** shows quadratic growth. **Not an efficient sorting method**.
- **Merge Sort** shows linearithmic growth. **Very efficient**. 
- **Counting Sort** shows linear growth. **Most efficient**.
- **SelectionSort** shows quadratic growth. **A better sorting method than BubbleSort**.
- **Quick Sort** shows linearithmic growth. 


## References

We used some help from chatgpt and did our research mostly on geeksforgeeks.org. 

- **ChatGPT Reference**: https://chatgpt.com/c/66eb8505-7cf8-8006-ae34-9dc5b74ab0a2
- **BubbleSort**: https://www.geeksforgeeks.org/bubble-sort-algorithm/
- **MergeSort**:  https://www.geeksforgeeks.org/merge-sort/
- **CountingSort**: https://www.geeksforgeeks.org/counting-sort/
- **SelectionSort**: https://www.geeksforgeeks.org/selection-sort-algorithm-2/
- **QuickSort**: https://www.geeksforgeeks.org/quick-sort-algorithm/
- **MatPlotLib**: https://www.geeksforgeeks.org/matplotlib-tutorial/ & https://www.youtube.com/watch?v=D4VlmL3G4_o

  
