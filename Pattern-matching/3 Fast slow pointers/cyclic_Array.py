def cyclic(arr):
    cyclic_index = []
    ptr = 0

    i = 0
    while i < len(arr):
        if arr[i] > 0:
            i += arr[i]
            # check if i jump out of right side
            if i > len(arr):
                i = i - len(arr)  # index - len(arr) - index
        else:
            i -= arr[i]
            # check if i  jump out from left side
            if i < 0:
                i = len(arr) - (i - arr[i])


arr = [2, 1, -1, -2]  # false
arr = [2, 2, -1, 2]  # true
print(cyclic(arr))
