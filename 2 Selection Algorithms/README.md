# **Random Select**

Random Select is an efficient algorithm for finding the i-th smallest element (order statistic) in an unsorted list without sorting the entire list. It is based on the idea of partitioning, similar to the QuickSort algorithm, but focuses only on the part of the list that could contain the desired element.

The algorithm works as follows:
1. **Partitioning**: Randomly select a pivot element from the list and partition the list into two sublists: elements less than or equal to the pivot, and elements greater than the pivot.
2. **Recursive Selection**:
   - If the pivot's position matches the desired order statistic (i), return the pivot as the answer.
   - If the desired order statistic is less than the pivot's position, recursively apply Random Select to the left sublist.
   - If the desired order statistic is greater, recursively apply Random Select to the right sublist, adjusting the order statistic accordingly.
3. **Termination**: The process continues until the sublist contains only one element, which is the answer.

By only processing the relevant part of the list at each step, Random Select achieves an average-case linear time complexity, making it much faster than sorting-based approaches when only a single order statistic is needed.

## **Function: `random_select(A, i)`**

Finds the i-th smallest element in the list `A` using the Random Select algorithm.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(random_select(A, 4))
# Output: 3
```

# **Deterministic Select**

Deterministic Select, also known as the Median of Medians algorithm, is a selection algorithm that finds the i-th smallest element (order statistic) in an unsorted list with guaranteed linear time in the worst case. Unlike Random Select, it uses a deterministic strategy to choose a good pivot, ensuring balanced partitioning at each step.

The algorithm operates as follows:
1. **Grouping**: Divide the list into groups of five elements each (the last group may have fewer than five).
2. **Find Medians**: Sort each group and find its median.
3. **Median of Medians**: Recursively apply Deterministic Select to the list of medians to find the median of medians, which is used as the pivot.
4. **Partitioning**: Partition the original list around the median of medians.
5. **Recursive Selection**:
   - If the pivot's position matches the desired order statistic (i), return the pivot as the answer.
   - If the desired order statistic is less than the pivot's position, recursively apply Deterministic Select to the left sublist.
   - If the desired order statistic is greater, recursively apply Deterministic Select to the right sublist, adjusting the order statistic accordingly.
6. **Termination**: The process continues until the sublist contains only one element, which is the answer.

By carefully choosing the pivot, Deterministic Select guarantees balanced partitions and linear time complexity, making it a robust choice for selection problems where worst-case performance is important.

## **Function: `deterministic_select(A, i)`**

Finds the i-th smallest element in the list `A` using the Deterministic Select (Median of Medians) algorithm.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(deterministic_select(A, 4))
# Output: 3
```

# **QuickSort Select**

QuickSort Select is a straightforward method for finding the i-th smallest element (order statistic) in an unsorted list. This approach first sorts the entire list using the QuickSort algorithm and then directly selects the (i-1)-th element from the sorted list.

The algorithm operates as follows:
1. **Sorting**: Apply the QuickSort algorithm to sort the entire list in ascending order.
2. **Selection**: After sorting, return the element at index (i-1), which corresponds to the i-th smallest element.

While this method is simple and guarantees correctness, it is less efficient than dedicated selection algorithms when only a single order statistic is needed, as it performs more work by fully sorting the list.

## **Function: `quicksort_select(A, i)`**

Finds the i-th smallest element in the list `A` by first sorting the list with QuickSort and then selecting the (i-1)-th element.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(quicksort_select(A, 4))
# Output: 3
```

# **Time Complexity**
- Random Select: Average-case $O(n)$, worst-case $O(n^2)$ (rare).
- Deterministic Select: Worst-case $O(n)$.
- QuickSort Select: Average-case $O(n \lg n)$, worst-case $O(n^2)$ (due to QuickSort's partitioning). This worst case can be avoided with the Randomized version of QuickSort, but it still remains less efficient than the dedicated selection algorithms for finding a single order statistic.