import random


def quick_sort(arr: list, start: int, end: int):
    if start >= end:
        return

    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    k = start - 1
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    for i in range(start, end):
        if arr[i] <= pivot:
            k += 1
            arr[k], arr[i] = arr[i], arr[k]

    arr[k + 1], arr[end] = arr[end], arr[k + 1]
    k += 1
    quick_sort(arr, start, k - 1)
    quick_sort(arr, k + 1, end)


if __name__ == "__main__":
    input_array = list(map(int, input("Enter an array: ").split()))
    e = len(input_array) - 1
    quick_sort(input_array, 0, e)
    print(*input_array, sep=' ')
