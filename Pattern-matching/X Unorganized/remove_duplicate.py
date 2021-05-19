def remove_dup(arr):
    # Time and space : O(N), O(1)
    fptr = 0
    sptr = 1
    arr_len = len(arr)
    while sptr < arr_len:
        if arr[sptr] != arr[fptr]:
            arr[fptr + 1] = arr[sptr]
            fptr += 1
        sptr += 1

    return fptr + 1


print(remove_dup([2, 3, 3, 3, 6, 9, 9]))

print(remove_dup([2, 2, 2, 11]))
