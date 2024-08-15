import random
import timeit

# Python3 code to linearly search x in arr[]
def linearSearch(arr, x):
    operations = 0
    for i in range(len(arr)):
        operations += 1
        if arr[i] == x:
            print("Linear search operations:", operations)
            return i, operations
    print("Linear search operations:", operations)
    return -1, operations

# Python3 code to implement iterative Binary Search
def binarySearch(arr, low, high, x):
    operations = 0
    while low <= high:
        operations += 1
        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            print("Binary search operations:", operations)
            return mid, operations

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    print("Binary search operations:", operations)
    return -1, operations

# Driver Code
if __name__ == '__main__':
    # Generate a sorted array for binary search
    arr = sorted([random.randint(1, 1000) for _ in range(200)])
    x = random.choice(arr)  # The value to search for

    # Measure execution time for Linear Search
    iter = 10
    ltime = timeit.timeit(lambda: linearSearch(arr, x)[1], number=iter)

    # Measure execution time for Binary Search
    btime = timeit.timeit(lambda: binarySearch(arr, 0, len(arr) - 1, x)[1], number=iter)

    # Print results
    print("Linear search took:", ltime)
    print("Binary search took:", btime)
