def swap(array, i, j):
    tempValue = array[j]
    array[j] = array[i]
    array[i] = tempValue
    return array

def partition(arr, start, end):
    pivotIndex = start
    pivotElement = arr[pivotIndex]
    while start < end:
        while arr[start] <= pivotElement and start < len(arr) - 1:
            start += 1
        while arr[end] > pivotElement:
            end -= 1
        if start < end:
            swap(arr, start, end)
    swap(arr, pivotIndex, end)
    return end

def quickSort(arr, start, end):
    if start < end:
        pivotIndex = partition(arr, start, end)
        quickSort(arr, 0, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, end)
    return arr

unsortedArray = [12, 32, 45, 61, 32, 78, 8, 93]
sortedArray = quickSort(unsortedArray, 0, len(unsortedArray) - 1)
print(sortedArray)