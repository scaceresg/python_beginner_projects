# Binary search algorithm:
# Binary search is a divide and conquer algorithm, which actually helps you search an ordered list
# faster than just scanning every single element.
# Assume that we have a list of ordered elements from least to greatest, and we need to find a target in
# the list where if it is, then return its index.
# The algorithm works finding the middle element in list, check if this is equals to, greater than
# or lower than the target, so we can disregard searching anything to the right of the list (if middle
# element is greater than the target) or to the left of the list (if middle element is lower than the target).
# This process is repeated on each segment after dividing until the target is found.

# We will prove that binary search is faster than naive search (for loops)

import random
import time


# Define a naive search function
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# Define the binary search function for a SORTED list
def binary_search(l, target, low=None, high=None):
    # Low and high helps to divide the list
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    # No target in list
    if high < low:
        return -1

    # Step 1. Find a midpoint
    midpoint = (low + high) // 2

    # Step 2. Evaluate if midpoint is ==, < or > target and divide
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:  # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)


# Proving that Binary search is more efficient than Naive search
if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    # build sorted list of length 10000
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # Check time before and after Naive Search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Navie search time: ", (end - start)/length, "seconds")

    # Check time before and after Binary Search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")