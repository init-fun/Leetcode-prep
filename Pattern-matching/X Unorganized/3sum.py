def threesum(arr, target):
    res = []
    arr.sort()  # O(nlogn)

    for i, val in enumerate(arr):
        if i > 0 and arr[i - 1] == val:
            continue

        left = i + 1
        right = len(arr) - 1

        while left < right:
            new_sum = val + arr[left] + arr[right]
            if new_sum > target:
                right -= 1
            elif new_sum < target:
                left += 1
            else:
                res.append([val, arr[left], arr[right]])  # we got our triplet
                left += 1

    # removing duplicate

    fptr = 0
    sptr = 1
    while sptr < len(res):
        if res[sptr] == res[sptr - 1]:
            fptr += 1
        sptr += 1
    return res[fptr:]


arr = [-3, 0, 1, 2, -1, 1, -2]
target = 3
arr = [-3, 0, 1, 2, -1, 1, -2]
target = 0
print(threesum(arr, target))