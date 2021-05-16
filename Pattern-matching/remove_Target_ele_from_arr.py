def remove_ele(arr, key):
    fptr = 0
    sptr = 0

    while sptr < len(arr):
        if arr[sptr] == key:
            arr[fptr], arr[sptr] = arr[sptr], arr[fptr]
            fptr += 1
        sptr += 1
    return len(arr) - fptr


# arr = [3, 2, 3, 6, 3, 10, 9, 3]
arr = [2, 11, 2, 2, 1]

print(remove_ele(arr, 2))