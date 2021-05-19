def sq_num(num):
    tmp = 0
    for i in str(num):
        tmp += int(i) ** 2
    return tmp


def happy(num):
    tmp_sum = []
    while str(num) != "1":
        num = sq_num(num)
        if num in tmp_sum:
            return False
        else:
            tmp_sum.append(num)

    return True


n = 12
print(happy(n))


n = 23
print(happy(n))