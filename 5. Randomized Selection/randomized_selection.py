import random


def randomized_selection(arr: list, start: int, end: int, order: int) -> int:
    if start == end:
        return arr[start]

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

    if k == order:
        return arr[k]
    elif k > order:
        num = randomized_selection(arr, start, k - 1, order)
    else:
        num = randomized_selection(arr, k + 1, end, order)

    return num


if __name__ == "__main__":
    input_array = list(map(int, input("Enter an array: ").split()))
    n = int(input("Enter the order statistic: "))
    e = len(input_array) - 1
    res = randomized_selection(input_array, 0, e, n - 1)
    print(res)
