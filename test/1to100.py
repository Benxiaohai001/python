def add_sum(n):
    if n == 1:
        return 1
    else:
        sum = n + add_sum(n - 1)
    return sum


print(add_sum(100))
def substr_num(fu_str, zi_str):
    for i in zi_str:
        if i not in fu_str:
            return 0
        else:
            for j in fu_str:
                