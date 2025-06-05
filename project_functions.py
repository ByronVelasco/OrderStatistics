import random


def min_value(A):
	# Assume the first element is the minimum initially
	minimum = A[0]
	# Iterate through the rest of the list
	for i in range(1, len(A)):
		# If a smaller element is found, update min
		if A[i] < minimum:
			minimum = A[i]
	# Return the smallest value found
	return minimum


def max_value(A):
	# Assume the first element is the maximum initially
	maximum = A[0]
	# Iterate through the rest of the list
	for i in range(1, len(A)):
		# If a larger element is found, update max
		if A[i] > maximum:
			maximum = A[i]
	# Return the largest value found
	return maximum


def min_and_max(A):
	# Call min_value to get the minimum and max_value to get the maximum
	return min_value(A), max_value(A)


# Returns both the minimum and maximum values in the list A using fewer comparisons
def min_and_max_optimized(A):
	n = len(A)
	# If the list has an even number of elements, initialize min and max by comparing the first two
	if n % 2 == 0:
		minimum, maximum = (A[0], A[1]) if A[0] < A[1] else (A[1], A[0])
		start = 2  # Start from the third element
	else:
		# If odd, initialize both to the first element
		minimum = maximum = A[0]
		start = 1  # Start from the second element

	# Process pairs of elements
	for i in range(start, n, 2):
		if A[i] < A[i + 1]:
			if A[i] < minimum:
				minimum = A[i]
			if A[i + 1] > maximum:
				maximum = A[i + 1]
		else:
			if A[i + 1] < minimum:
				minimum = A[i + 1]
			if A[i] > maximum:
				maximum = A[i]
	# Return the minimum and maximum found
	return minimum, maximum


def partition(A, p, r):
	pivot = A[r]  # Choose the last element as the pivot
	i = p - 1  # Initialize the index for the smaller element
	for j in range(p, r):
		if A[j] <= pivot:  # If the current element is less than or equal to the pivot
			i += 1  # Increment the index for the smaller element
			A[i], A[j] = A[j], A[i]  # Swap the elements
	A[i + 1], A[r] = A[r], A[i + 1]  # Place the pivot in its correct position
	return i + 1  # Return the index of the pivot


def random_partition(A, p, q):
	pivot_index = random.randint(p, q)  # Randomly select a pivot index
	A[pivot_index], A[q] = A[q], A[pivot_index]  # Swap the pivot with the last element
	return partition(A, p, q)  # Perform standard partitioning


def random_select(A, i, p=0, q=None):
	# Ensure q is set only once at the start of the recursion
	if q is None:
		q = len(A) - 1
	def _random_select(A, i, p, q):
		# If the subarray has only one element, return it
		if p == q:
			return A[p]
		# Partition the array randomly and get the pivot index
		pivot_index = random_partition(A, p, q)
		# Number of elements on the left including the pivot
		k = pivot_index - p + 1
		# If the pivot is the i-th smallest, return it
		if i == k:
			return A[pivot_index]
		# If the i-th smallest is in the left partition, recurse on the left
		elif i < k:
			return _random_select(A, i, p, pivot_index - 1)
		# Otherwise, recurse on the right partition with adjusted i
		else:
			return _random_select(A, i - k, pivot_index + 1, q)
	return _random_select(A, i, p, q)


def partition_around(A, p, r, pivot_value):
	# Move the pivot_value to the end of the subarray
	for i in range(p, r + 1):
		if A[i] == pivot_value:
			A[i], A[r] = A[r], A[i]
			break
	pivot = A[r]  # The pivot is now at the end
	i = p - 1  # Index of the smaller element
	# Rearrange elements so that those <= pivot are on the left
	for j in range(p, r):
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	# Place the pivot in its correct position
	A[i + 1], A[r] = A[r], A[i + 1]
	# Return the index of the pivot after partitioning
	return i + 1


def deterministic_select(A, i, p=0, r=None):
	# Set r to the last index if not provided (only once at the beginning)
	if r is None:
		r = len(A) - 1

	def _select(A, i, p, r):
		# Handle the case where the number of elements is not a multiple of 5
		while (r - p + 1) % 5 != 0:
			# Move the smallest element in A[p:r+1] to the front
			for j in range(p + 1, r + 1):
				if A[p] > A[j]:
					A[p], A[j] = A[j], A[p]
			# If looking for the smallest, return it
			if i == 1:
				return A[p]
			# Otherwise, move to the next subarray and decrement i
			p = p + 1
			i = i - 1

		g = (r - p + 1) // 5  # number of groups of 5
		# Sort each group of 5 and write back to A
		for j in range(p, p + g):
			group = [A[j + k * g] for k in range(5)]
			group.sort()
			for k in range(5):
				A[j + k * g] = group[k]

		# The medians are in the middle fifth of A[p:r]
		# Recursively find the median of medians
		x = _select(A, g // 2 + 1, p + 2 * g, p + 3 * g - 1)

		# Partition around the median of medians
		q = partition_around(A, p, r, x)
		k = q - p + 1  # Number of elements on the left including the pivot

		# Return the correct order statistic
		if i == k:
			return A[q]
		elif i < k:
			return _select(A, i, p, q - 1)
		else:
			return _select(A, i - k, q + 1, r)

	return _select(A, i, p, r)


def quick_sort(A, p=0, r=None):
	if r is None:  # Evaluate this condition only once
			r = len(A) - 1

	def recursive_quick_sort(A, p, r):
		if p < r:  # Base case: stop when the sublist has one or no elements
			pivot_index = partition(A, p, r)  # Partition the list and get the pivot index
			recursive_quick_sort(A, p, pivot_index - 1)  # Recursively sort the left partition
			recursive_quick_sort(A, pivot_index + 1, r)  # Recursively sort the right partition

	# Call the inner recursive function
	recursive_quick_sort(A, p, r)


def quicksort_select(A, i):
	quick_sort(A)  # Sort the array first
	return A[i - 1]  # Return the i-th smallest element