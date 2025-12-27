#include <stdio.h>
#include <stdlib.h>

// MERGE SORT
void conquer(int arr[], int si, int mid, int ei) {
    int *merger = (int *)malloc((ei - si + 1) * sizeof(int));
    if (merger == NULL) {  // Check if malloc succeeded
        printf("Memory allocation failed\n");
        exit(1);
    }

    int i = si;
    int j = mid + 1;
    int k = 0;

    // Merge the two halves
    while (i <= mid && j <= ei) {
        if (arr[i] < arr[j]) {
            merger[k++] = arr[i++];
        } else {
            merger[k++] = arr[j++];
        }
    }

    // Handle remaining elements of the left half
    while (i <= mid) {
        merger[k++] = arr[i++];
    }

    // Handle remaining elements of the right half
    while (j <= ei) {
        merger[k++] = arr[j++];
    }

    // Copy merged elements back to the original array
    for (i = si, k = 0; i <= ei; i++, k++) {
        arr[i] = merger[k];
    }

    free(merger); // Free the dynamically allocated memory
}

void divide(int arr[], int si, int ei) {
    if (si >= ei) {
        return;
    }

    int mid = si + (ei - si) / 2;
    divide(arr, si, mid);      // Left half
    divide(arr, mid + 1, ei);  // Right half
    conquer(arr, si, mid, ei);
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));  // Corrected malloc usage
    if (arr == NULL) {  // Check if malloc succeeded
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Enter space-separated elements:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    divide(arr, 0, n - 1);

    printf("Sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr); // Free dynamically allocated memory
    return 0;
}

