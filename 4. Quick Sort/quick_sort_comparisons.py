def partition_first(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


def quick_sort_first(arr, low, high):
    if low < high:
        comparisons.append(high - low)
        pivot_index = partition_first(arr, low, high)
        quick_sort_first(arr, low, pivot_index - 1)
        quick_sort_first(arr, pivot_index + 1, high)


def partition_last(arr, low, high):
    arr[low], arr[high] = arr[high], arr[low]
    return partition_first(arr, low, high)


def quick_sort_last(arr, low, high):
    if low < high:
        comparisons.append(high - low)
        pivot_index = partition_last(arr, low, high)
        quick_sort_last(arr, low, pivot_index - 1)
        quick_sort_last(arr, pivot_index + 1, high)


def median_of_three(arr, low, high):
    mid = low + (high - low) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[low] = arr[low], arr[mid]
    return low


def partition_median(arr, low, high):
    median_index = median_of_three(arr, low, high)
    pivot = arr[median_index]
    arr[median_index], arr[low] = arr[low], arr[median_index]  # Move pivot to the first position
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Move pivot to the correct position
    return i - 1


def quick_sort_median(arr, low, high):
    if low < high:
        comparisons.append(high - low)
        pivot_index = partition_median(arr, low, high)
        quick_sort_median(arr, low, pivot_index - 1)
        quick_sort_median(arr, pivot_index + 1, high)


if __name__ == "__main__":
    with open("QuickSort.txt", 'r') as file:
        input_array = [int(line.strip()) for line in file]

    # Quick Sort with First Element as Pivot
    comparisons = []
    quick_sort_first(input_array.copy(), 0, len(input_array) - 1)
    print("Total comparisons (first element as pivot):", sum(comparisons))

    # Quick Sort with Last Element as Pivot
    comparisons = []
    quick_sort_last(input_array.copy(), 0, len(input_array) - 1)
    print("Total comparisons (last element as pivot):", sum(comparisons))

    # Quick Sort with Median of Three as Pivot
    comparisons = []
    quick_sort_median(input_array.copy(), 0, len(input_array) - 1)
    print("Total comparisons (median of three as pivot):", sum(comparisons))
