def count_inversions(arr):
    if len(arr) <= 1:
        return 0

    half = len(arr) // 2
    first = arr[:half]
    second = arr[half:]
    x = count_inversions(first)
    y = count_inversions(second)
    i = j = k = 0
    inversions = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            inversions += len(first) - i
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

    return x + y + inversions


if __name__ == "__main__":
    with open("IntegerArray.txt", 'r') as file:
        numbers = [int(line.strip()) for line in file]
    res = count_inversions(numbers)
    print(res)
