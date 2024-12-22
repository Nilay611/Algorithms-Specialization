def merge_sort(arr):
    if len(arr) <= 1:
        return

    half = len(arr) // 2
    first = arr[:half]
    second = arr[half:]
    merge_sort(first)
    merge_sort(second)
    i = j = k = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            j += 1
        k += 1

    while i < len(first):
        arr[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        arr[k] = second[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = list(map(int, input("Enter an array: ").split()))
    merge_sort(arr)
    print(*arr, sep=' ')
