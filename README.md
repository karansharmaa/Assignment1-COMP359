Our task for this assignment was: "Plot the runtimes for sorting input arrays of different sizes, at least for a quadratic sort, and a linearithmic sort. Are the runtime plots shaped as we would expect from their analyses?"
And as a result, we chose bubble sort, merge sort and bucket sort as our sorting algorithms for this assignment. 

The complexities for them as follow: 
1. Bubble Sort: Quadratic O(n^2).
2. Merge Sort: Linearthimic O(n log n).
3. Bucket Sort: Linear O(n + k) -> O(n).

After some research into the sorting algorithms, we were able to code them to existence (which is in the assignment1.py file). (Karan did the coding part). 

Now, **what were we exactly sorting?** 
- Before getting items to sort, we had to determine how big our arrays were going to be. We had to work in ascending order - as the assumption is, the bigger the array, the more time it takes to sort. And so we took the sizes of: 
100,200,400,800,1600,3200,5000 and put them into a numpy array named "sizes". 
- Then, we used for loops to iterate through these values and create arrays of each individual sizes. 
- Once we had that, we used math.random to put values between 0 and 10000 into these arrays and applied the sorting algorithms to them.
- Then, we used the matplotlib library to create a graph which plotted the values of the runtimes onto the said grapha and displayed it in a GUI as output.

The output was as follows: ![image](https://github.com/user-attachments/assets/44d13671-0411-4e3f-8637-c2887712cfaa)

From our observation, we can say that the runtime plots **are** shaped as we would expect from their analyses. 
- Bubble sort shows a quadratic growth in graph. 
- Merge sort shows linearitmic growth. 
- Bucket sort exhibits linear growth in this case. Normally, bucket sort has a time complexity of O(n+k), where n is the number of elements and k is the number of buckets. In this instance, it appears that k is very small or 
effectively zero, which could explain the observed linear behavior on the graph. Understanding why k behaves this way in this context was challenging.

  
