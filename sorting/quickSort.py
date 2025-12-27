# QUICK SORT (pivot = first element)

def partition(arr, si, ei):
    pivot = arr[si]        # pivot at start
    i = si + 1
    j = ei

    while True:
        while i <= ei and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # place pivot in correct position
    arr[si], arr[j] = arr[j], arr[si]
    return j


def divide(arr, si, ei):
    if si >= ei:
        return

    p = partition(arr, si, ei)
    divide(arr, si, p - 1)   # left subarray
    divide(arr, p + 1, ei)   # right subarray


# ---- main ----
n = int(input("Enter the number of elements: "))
