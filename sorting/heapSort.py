# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Build a max heap
def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# Insert a new element (append)
def append(arr, key):
    arr.append(key)  # add at the end
    i = len(arr) - 1
    parent = (i - 1) // 2

    # Fix heap property by moving up
    while i > 0 and arr[parent] < arr[i]:
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent
        parent = (i - 1) // 2


# Remove and return the max element (pop)
def pop(arr):
    n = len(arr)
    if n == 0:
        return None

    root = arr[0]                # max element
    arr[0] = arr[-1]             # move last to root
    arr.pop()                    # remove last
    heapify(arr, len(arr), 0)    # fix heap property
    return root


# Heap sort using the heap functions
def heap_sort(arr):
    n = len(arr)
    build_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)

    # Build heap
    build_heap(arr)
    print("Heap:", arr)

    # Insert (append)
    append(arr, 20)
    print("After append 20:", arr)

    # Remove max (pop)
    max_val = pop(arr)
    print("Popped max:", max_val)
    print("Heap after pop:", arr)

    # Heap sort
    heap_sort(arr)
    print("Sorted array:", arr)