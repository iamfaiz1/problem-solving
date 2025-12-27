# MERGE SORT

def conquer(arr, si, mid, ei):
    merger = [0] * (ei - si + 1)
    i = si
    j = mid + 1
    k = 0

    # Merge the two halves
    while i <= mid and j <= ei:
        if arr[i] < arr[j]:
            merger[k] = arr[i]
            i += 1
        else:
            merger[k] = arr[j]
            j += 1
        k += 1

    # Remaining elements of left half
    while i <= mid:
        merger[k] = arr[i]
        i += 1
        k += 1

    # Remaining elements of right half
    while j <= ei:
        merger[k] = arr[j]
        j += 1
        k += 1

    # Copy back to original array
    for idx in range(len(merger)):
        arr[si + idx] = merger[idx]


def divide(arr, si, ei):
    if si >= ei:
        return
    
    mid = si + (ei - si) // 2
    divide(arr, si, mid)  # Left half
    divide(arr, mid + 1, ei)  # Right half
    conquer(arr, si, mid, ei)


# ---- main ----
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter space-separated elements:\n").split()))

divide(arr, 0, n - 1)

print("Sorted array:")
print(*arr)
