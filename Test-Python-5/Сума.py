def sum_range(a, b):
    if a > b:
        a, b = b, a
    total = sum(range(a, b + 1))
    print(total)
    return total

sum_range(3, 20)