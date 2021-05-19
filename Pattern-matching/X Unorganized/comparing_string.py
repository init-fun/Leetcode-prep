def compare(a, b):
    x = new_fun(a)
    y = new_fun(b)
    return x == y


def new_fun(arr):
    # single length string
    if len(arr) == 1:
        if arr[0] == "#":
            return ""
        else:
            return arr

    # more than one char
    res = ""
    fptr = 0
    sptr = 1
    rem_len = len(arr) - 1
    while sptr < len(arr) and fptr < len(arr) - 1:
        # check for pair
        if arr[fptr] != "#" and arr[sptr] == "#":
            fptr += 2
            sptr += 2
            if abs(sptr - rem_len) == 1:
                break
        else:
            # this is not the pair
            res += arr[fptr]
            fptr += 1
            sptr += 1

    last_index = len(arr) - 1
    if arr[last_index] == "#":
        return res
    else:
        res += arr[last_index]
    return res


print(compare("xy#z", "xzz#"))

# print(new_fun("xy#z#x"))
