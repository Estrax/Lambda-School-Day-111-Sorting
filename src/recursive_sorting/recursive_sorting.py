# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0
    while j < len(arrA) and k < len(arrB):
        if arrA[j] <= arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1
        i += 1
    while j < len(arrA):
        merged_arr[i] = arrA[j]
        j += 1
        i += 1
    while k < len(arrB):
        merged_arr[i] = arrB[k]
        k += 1
        i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    tmp = mid + 1

    if arr[mid] <= arr[mid+1]:  # the merge points are sorted
        return arr

    while start <= mid and tmp <= end:
        if arr[start] <= arr[tmp]:
            start += 1
        else:
            value = arr[tmp]
            index = tmp

            while index != start:
                arr[index] = arr[index-1]
                index -= 1
            arr[start] = value

            start += 1
            mid += 1
            tmp += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if r-l > 0:
        m = l+(r-l)//2
        arr = merge_sort_in_place(arr, l, m)
        arr = merge_sort_in_place(arr, m+1, r)
        arr = merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    if len(arr) < 64:
        for i in range(len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key <= arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    else:
        runs = []
        sorted_runs = []
        arr_len = len(arr)
        new_run = [arr[0]]

        for i in range(1, arr_len):
            if i == arr_len-1:
                new_run.append(arr[i])
                runs.append(new_run)
                break
            if arr[i] < arr[i-1]:
                if not new_run:
                    runs.append([arr[i]])
                    new_run.append(arr[i])
                else:
                    runs.append(new_run)
                    new_run = []
            else:
                new_run.append(arr[i])
        for run in runs:
            for i in range(len(run)):
                key = run[i]
                j = i - 1
                while j >= 0 and key <= run[j]:
                    run[j+1] = run[j]
                    j -= 1
                run[j+1] = key
            sorted_runs.append(run)

        sorted_arr = []
        for run in sorted_runs:
            sorted_arr = merge(sorted_arr, run)
        return sorted_arr

    return arr
