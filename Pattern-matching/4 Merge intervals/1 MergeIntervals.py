def merge_intervals(arr):
    # sort the arr by first ele
    # take a new arr for the result

    arr.sort(key=lambda x: x[0])  # O(nlogn)
    res = []

    start = arr[0][0]
    end = arr[0][1]

    for i in range(1, len(arr)):  # O(n)
        # i has our new interval
        if i[0] <= end:  # sec interval falls  into the first
            end = max(i[1], end)  # fix the end interval
        else:
            res.append([start, end])
            start = i[0]
            end = i[1]

    res.append([start, end])
    return res


arr = [[1, 4], [2, 5], [7, 9]]
print(merge_intervals(arr))