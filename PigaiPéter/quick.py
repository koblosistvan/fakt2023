def partition(arr, low, high):
    store_index = low - 1
    pivot = (arr[high])
    for i in range(low, high):
        if arr[i] <= pivot:
            store_index += 1
            arr[store_index], arr[i] = arr[i], arr[store_index]
    arr[store_index + 1], arr[high] = arr[high], arr[store_index +1]
    return store_index + 1
def quicksort(arr,low,high):
    if low < high:
        part_index = partition(arr,low,high)
        quicksort(arr, low, part_index-1)
        quicksort(arr, part_index, high)
    return arr

arrr = [1, 7, 4, 1, 10, 9, -2]
print(quicksort(arrr, 0, len(arrr) - 1))
