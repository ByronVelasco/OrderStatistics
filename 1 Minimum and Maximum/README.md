# **Minimum**

To find the minimum value in a list by searching all elements, we start by assuming the first element is the smallest. We then iterate through each remaining element in the list, comparing it to our current minimum. If a smaller element is found, we update our minimum. After checking every element, the value stored as the minimum is the smallest in the list.

## **Function: `min_value(A)`**

Searches through the list `A` to find the minimum value.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(min_value(A))
# Output: 1
```

# **Maximum**

To find the maximum value in a list by searching all elements, we start by assuming the first element is the largest. We then iterate through each remaining element in the list, comparing it to our current maximum. If a larger element is found, we update our maximum. After checking every element, the value stored as the maximum is the largest in the list.

## **Function: `max_value(A)`**

Searches through the list `A` to find the maximum value.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(max_value(A))
# Output: 9
```

# **Minimum and Maximum**

To find both the minimum and maximum values in a list, we can combine the two previous functions into one.

## **Function: `min_and_max(A)`**

Searches through the list `A` to find both the minimum and maximum values.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_val, max_val = min_and_max(A)
print(f"Minimum: {min_val}, Maximum: {max_val}")
# Output: Minimum: 1, Maximum: 9
```

# **Optimized Minimum and Maximum**

The optimized approach for finding both the minimum and maximum values in a list works by processing elements in pairs. For each pair, the two elements are first compared to each other, and then the smaller is compared to the current minimum while the larger is compared to the current maximum. This reduces the total number of comparisons needed compared to checking each element individually against both the minimum and maximum. If the list has an odd number of elements, the first element is used to initialize both the minimum and maximum before proceeding with pairwise comparisons. This method achieves greater efficiency, especially for large lists.

## **Function: `min_and_max_optimized(A)`**

Searches through the list `A` to find both the minimum and maximum values using an optimized approach.

### **Example:**

```python
A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_val, max_val = min_and_max_optimized(A)
print(f"Minimum: {min_val}, Maximum: {max_val}")
# Output: Minimum: 1, Maximum: 9
```

# **Time Complexity**

The time complexity for all the functions is $O(n)$, where $n$ is the number of elements in the list. This is because each function iterates through the list at least once to find the minimum and/or maximum values. In the case of the optimized function, its constant factor is lower due to the pairwise comparisons, but it still operates in linear time.