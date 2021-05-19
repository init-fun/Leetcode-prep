def target_sum(arr, target):
#   space and time -> O(1) and O(N)
    # fptr = 0
    # sptr = len(arr) - 1

    # while fptr != sptr:
    #     new_total = arr[fptr] + arr[sptr]
    #     if new_total == target:
    #         return [fptr, sptr]
    #     elif new_total < target:
    #         fptr += 1
    #     elif new_total > target:
    #         sptr -= 1
    # else:
    #     print("Not found")
    #     return

# space and time -> O(N)

    # nums = {}
    # for index, val in enumerate(arr):
    #     target_sum = target - val
    #     if target_sum not in nums:
    #         # insert it into the dict
    #         nums[val] = index
    #     else:
    #         return [nums[target_sum], index]

print(target_sum([1, 2, 3, 4, 6], 6))
print(target_sum([2, 5, 9, 11], 11))
