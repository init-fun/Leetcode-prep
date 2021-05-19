def contain_overlap(arr):
    if len(arr) == 1:
        return arr

    arr.sort(key=lambda x: x[0])

    start = arr[0][0]
    end = arr[0][1]

    for i in range(1, len(arr)):
        if arr[i][0] < end:
            return True
        else:
            start = arr[i][0]
            end = arr[i][1]

    return False


arr = [[1, 4], [4, 5], [7, 9]]
print(contain_overlap(arr))