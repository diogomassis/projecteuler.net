def brute_force(n: int) -> int:
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def sum_of(d: int, n: int) -> int:
    return int(d * int(n / d) * (1 + int(n / d)) / 2)


result_brute_force = brute_force(1000)
print(result_brute_force)

result = sum_of(3, 999) + sum_of(5, 999) - sum_of(15, 999)
print(result)
