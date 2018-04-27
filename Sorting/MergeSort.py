def merge(a, b, arr):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1


def mergeSort(A):
    # base case
    if len(A) < 2:
        return

    # initial two list to store lists split from A
    mid = int(len(A) / 2)
    left = [0] * mid
    right = [0] * (len(A) - mid)

    # copy left part of A to left
    for i in range(mid):
        # i = 0, 1, ... , mid-2, mid-1
        left[i] = A[i]
    for i in range(mid, len(A)):
        # i = mid, mid+1, ... len(A) - mid - n - 1
        right[i - mid] = A[i]
        # index range of right: 0 - mid

    mergeSort(left)
    mergeSort(right)
    merge(left, right, A)

