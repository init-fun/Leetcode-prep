def sorted_sq(arr):
    # time and space : O(n) and O(1) cause inplace
    # for i, v in enumerate(arr):
    #     arr[i] = arr[i] ** 2
    # # most probabily O(nlogn)
    # return sorted(arr)

    # result : O( N logN )

    len_arr = len(arr)
    res_arr = [0 for i in range(len_arr)]
    res_index = len_arr - 1

    fptr = 0
    sptr = len_arr - 1

    while fptr < sptr:
        left_sq = arr[fptr] ** 2
        right_sq = arr[sptr] ** 2

        if left_sq > right_sq:
            res_arr[res_index] = left_sq
            fptr += 1
        else:
            res_arr[res_index] = right_sq
            sptr -= 1

        res_index -= 1

    return res_arr
    # Time and spacce : O(N)


arr = [-2, -1, 0, 2, 3]
print(sorted_sq(arr))