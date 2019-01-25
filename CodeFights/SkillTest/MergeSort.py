def merge_sort(arr):
    mergeSort(arr, 0, len(arr) - 1)
    return arr

def merge(arr, l, m, r):
    if (arr[m] > arr[m + 1]):
        # Left Buffer
        L = arr[l:m + 1]
        # Right Buffer
        R = arr[m + 1:r + 1]

        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        # Length of both the buffers
        len_l = m + 1 - l
        len_r = r - m

        # Merging of two sorted subarrays
        while i < len_l and j < len_r:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy if there are any elements in the left subarray
        # Note that the right subarray is already there and hence does not need to be copied
        while (i < len_l):
            arr[k] = L[i]
            i += 1
            k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        # Sort first and second subarray
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Merge both the subarrays
        merge(arr, l, m, r)

print(merge_sort([5,1,7,3,2,8,6,4]))